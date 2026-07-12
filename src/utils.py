"""Shared network, date, text-cleaning, and deduplication helpers."""
from __future__ import annotations

import html
import logging
import re
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime
from typing import Any, Iterable
from urllib.parse import urlsplit, urlunsplit

import requests

from config import LOOKBACK_DAYS, REQUEST_TIMEOUT, TIMEZONE, USER_AGENT

LOGGER = logging.getLogger(__name__)


def get_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json, application/atom+xml, application/rss+xml, text/xml, */*"})
    return session


def safe_get(session: requests.Session, url: str, **kwargs: Any) -> requests.Response | None:
    """GET with a mandatory timeout; callers can safely skip a failed source."""
    try:
        response = session.get(url, timeout=REQUEST_TIMEOUT, **kwargs)
        response.raise_for_status()
        return response
    except requests.RequestException as exc:
        LOGGER.warning("Unable to fetch %s: %s", url, exc)
        return None


def clean_text(value: str | None) -> str:
    text = html.unescape(value or "")
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_date(value: Any) -> datetime | None:
    """Parse common API/RSS date representations into Asia/Taipei time."""
    if not value:
        return None
    if isinstance(value, datetime):
        dt = value
    elif isinstance(value, tuple):
        dt = datetime(*value[:6], tzinfo=TIMEZONE)
    else:
        raw = str(value).strip()
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            try:
                dt = parsedate_to_datetime(raw)
            except (TypeError, ValueError):
                return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=TIMEZONE)
    return dt.astimezone(TIMEZONE)


def within_lookback(dt: datetime | None, now: datetime, days: int = LOOKBACK_DAYS) -> bool:
    return bool(dt and now - timedelta(days=days) <= dt <= now + timedelta(hours=6))


def canonical_url(url: str) -> str:
    parts = urlsplit(url.strip())
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), "", ""))


def deduplicate(items: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    result = []
    for item in items:
        title_key = re.sub(r"\W+", "", item.get("title", "").lower())
        key = canonical_url(item.get("link", "")) or title_key
        if key and key not in seen:
            seen.add(key)
            result.append(item)
    return result


def extractive_summary(text: str, max_chars: int = 320) -> str:
    cleaned = clean_text(text)
    if not cleaned:
        return "No summary was provided by the source."
    sentences = re.split(r"(?<=[.!?。！？])\s+", cleaned)
    summary = " ".join(sentences[:2])
    return summary if len(summary) <= max_chars else summary[: max_chars - 1].rstrip() + "…"

