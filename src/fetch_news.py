"""Fetch recent AI industry posts from configured RSS/Atom feeds."""
from __future__ import annotations

from datetime import datetime

import feedparser

from config import NEWS_FEEDS
from utils import clean_text, deduplicate, get_session, parse_date, safe_get, within_lookback


def fetch_news(now: datetime) -> list[dict]:
    session = get_session()
    items = []
    for source, url in NEWS_FEEDS.items():
        response = safe_get(session, url)
        if not response:
            continue
        for entry in feedparser.parse(response.content).entries:
            published = parse_date(entry.get("published") or entry.get("updated") or entry.get("published_parsed"))
            if within_lookback(published, now):
                items.append({
                    "kind": "news", "title": clean_text(entry.get("title")),
                    "source": source, "date": published, "link": entry.get("link", ""),
                    "summary": clean_text(entry.get("summary") or entry.get("description")),
                })
    return deduplicate(items)

