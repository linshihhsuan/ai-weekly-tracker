"""Fetch recent papers from the public arXiv Atom API."""
from __future__ import annotations

from datetime import datetime
from urllib.parse import quote

import feedparser

from config import PAPER_CATEGORIES, PAPER_KEYWORDS
from utils import clean_text, deduplicate, get_session, parse_date, safe_get, within_lookback


def fetch_papers(now: datetime) -> list[dict]:
    session = get_session()
    category_query = " OR ".join(f"cat:{cat}" for cat in PAPER_CATEGORIES)
    keyword_query = " OR ".join(f'all:"{word}"' for word in PAPER_KEYWORDS)
    query = quote(f"({category_query}) AND ({keyword_query})", safe="")
    url = f"https://export.arxiv.org/api/query?search_query={query}&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending"
    response = safe_get(session, url)
    if not response:
        return []
    items = []
    for entry in feedparser.parse(response.content).entries:
        published = parse_date(entry.get("published"))
        if not within_lookback(published, now):
            continue
        items.append({
            "kind": "paper", "title": clean_text(entry.get("title")),
            "authors": [author.get("name", "") for author in entry.get("authors", [])],
            "source": "arXiv", "date": published, "link": entry.get("link", ""),
            "summary": clean_text(entry.get("summary")),
            "tags": [tag.get("term", "") for tag in entry.get("tags", [])],
        })
    return deduplicate(items)

