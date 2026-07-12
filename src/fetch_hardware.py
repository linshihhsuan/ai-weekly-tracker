"""Fetch hardware-focused RSS items and relevant papers/news."""
from __future__ import annotations

from datetime import datetime

import feedparser

from config import HARDWARE_FEEDS, HARDWARE_KEYWORDS
from utils import clean_text, deduplicate, get_session, parse_date, safe_get, within_lookback


def is_hardware_related(item: dict) -> bool:
    haystack = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    return any(keyword.lower() in haystack for keyword in HARDWARE_KEYWORDS)


def fetch_hardware(now: datetime, related_items: list[dict] | None = None) -> list[dict]:
    session = get_session()
    items = []
    for source, url in HARDWARE_FEEDS.items():
        response = safe_get(session, url)
        if not response:
            continue
        for entry in feedparser.parse(response.content).entries:
            published = parse_date(entry.get("published") or entry.get("updated") or entry.get("published_parsed"))
            item = {
                "kind": "hardware", "title": clean_text(entry.get("title")), "source": source,
                "date": published, "link": entry.get("link", ""),
                "summary": clean_text(entry.get("summary") or entry.get("description")),
            }
            if within_lookback(published, now) and is_hardware_related(item):
                items.append(item)
    for original in related_items or []:
        if is_hardware_related(original):
            copy = dict(original)
            copy["kind"] = "hardware"
            items.append(copy)
    return deduplicate(items)

