"""Search GitHub repositories using authenticated or low-rate public API calls."""
from __future__ import annotations

import os
from datetime import datetime, timedelta

from config import GITHUB_KEYWORDS
from utils import deduplicate, get_session, parse_date, safe_get, within_lookback


def fetch_github(now: datetime) -> list[dict]:
    session = get_session()
    token = os.getenv("GITHUB_TOKEN", "").strip()
    if token:
        session.headers.update({"Authorization": f"Bearer {token}", "X-GitHub-Api-Version": "2022-11-28"})
    # Combine terms into a few broad queries to preserve unauthenticated rate limits.
    queries = ["LLM RAG agent", "inference transformer quantization", "CUDA Triton vLLM", '"ml compiler" accelerator']
    since = (now - timedelta(days=7)).date().isoformat()
    items = []
    for terms in queries:
        response = safe_get(session, "https://api.github.com/search/repositories", params={
            "q": f"{terms} pushed:>={since}", "sort": "stars", "order": "desc", "per_page": 20,
        })
        if not response:
            continue
        for repo in response.json().get("items", []):
            updated = parse_date(repo.get("pushed_at") or repo.get("updated_at"))
            if within_lookback(updated, now):
                items.append({
                    "kind": "github", "title": repo.get("full_name", ""),
                    "source": "GitHub", "date": updated, "link": repo.get("html_url", ""),
                    "summary": repo.get("description") or "No repository description provided.",
                    "stars": repo.get("stargazers_count", 0), "language": repo.get("language") or "N/A",
                    "topics": repo.get("topics", []), "matched_keywords": GITHUB_KEYWORDS,
                })
    return deduplicate(items)

