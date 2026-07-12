"""Command-line entry point for the weekly AI tracker."""
from __future__ import annotations

import logging
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

# Permit both `python src/main.py` and module-style execution.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from config import MAX_ITEMS_PER_SECTION, ROOT_DIR, TIMEZONE  # noqa: E402
from fetch_github import fetch_github  # noqa: E402
from fetch_hardware import fetch_hardware  # noqa: E402
from fetch_news import fetch_news  # noqa: E402
from fetch_papers import fetch_papers  # noqa: E402
from generate_report import generate_report  # noqa: E402
from rank_items import rank_items  # noqa: E402


def main() -> int:
    load_dotenv(ROOT_DIR / ".env")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    now = datetime.now(TIMEZONE)
    logging.info("Collecting the previous 7 days relative to %s", now.isoformat())
    papers = fetch_papers(now)
    news = fetch_news(now)
    projects = fetch_github(now)
    hardware = fetch_hardware(now, papers + news)
    path = generate_report(
        now,
        rank_items(papers, now, MAX_ITEMS_PER_SECTION),
        rank_items(news, now, MAX_ITEMS_PER_SECTION),
        rank_items(projects, now, MAX_ITEMS_PER_SECTION),
        rank_items(hardware, now, MAX_ITEMS_PER_SECTION),
    )
    logging.info("Report created: %s", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

