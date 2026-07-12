"""Transparent, maintainable relevance ranking shared by all sections."""
from __future__ import annotations

import math
from datetime import datetime

from config import GITHUB_KEYWORDS, HARDWARE_KEYWORDS, PAPER_KEYWORDS

SIGNAL_KEYWORDS = ["code", "benchmark", "hardware", "efficiency", "latency", "throughput"]


def score_item(item: dict, now: datetime) -> float:
    date = item.get("date")
    age_days = max(0.0, (now - date).total_seconds() / 86400) if date else 30
    score = max(0.0, 35 - age_days * 5)  # freshness: 35 points today, fading over 7 days
    text = f"{item.get('title', '')} {item.get('summary', '')} {' '.join(item.get('topics', []))}".lower()
    general_hits = sum(keyword.lower() in text for keyword in PAPER_KEYWORDS + GITHUB_KEYWORDS)
    hardware_hits = sum(keyword.lower() in text for keyword in HARDWARE_KEYWORDS)
    signal_hits = sum(keyword in text for keyword in SIGNAL_KEYWORDS)
    score += min(general_hits * 4, 28) + min(hardware_hits * 6, 30) + min(signal_hits * 3, 15)
    if item.get("kind") == "github":
        score += min(math.log10(max(item.get("stars", 0), 1)) * 8, 32)
    return round(score, 2)


def rank_items(items: list[dict], now: datetime, limit: int) -> list[dict]:
    for item in items:
        item["score"] = score_item(item, now)
    return sorted(items, key=lambda item: (item["score"], item.get("date") or datetime.min.replace(tzinfo=now.tzinfo)), reverse=True)[:limit]

