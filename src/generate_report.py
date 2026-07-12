"""Create a readable Markdown digest with optional OpenAI-powered summaries."""
from __future__ import annotations

import logging
import os
from datetime import datetime

from config import HARDWARE_KEYWORDS, REPORTS_DIR
from utils import extractive_summary

LOGGER = logging.getLogger(__name__)


def _llm_summary(title: str, text: str, purpose: str) -> str | None:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        return None
    try:
        from openai import OpenAI
        response = OpenAI(api_key=api_key).responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            input=f"Summarize this item in one concise sentence for a weekly AI digest. Focus on {purpose}. Title: {title}\nText: {text[:3000]}",
        )
        return response.output_text.strip()
    except Exception as exc:  # LLM failure must never prevent report generation.
        LOGGER.warning("OpenAI summary failed; using extractive fallback: %s", exc)
        return None


def summarize(item: dict, purpose: str) -> str:
    return _llm_summary(item.get("title", ""), item.get("summary", ""), purpose) or extractive_summary(item.get("summary", ""))


def _date(item: dict) -> str:
    return item["date"].date().isoformat() if item.get("date") else "Unknown"


def _keywords(item: dict) -> list[str]:
    text = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    return [word for word in HARDWARE_KEYWORDS if word.lower() in text][:8]


def generate_report(now: datetime, papers: list[dict], news: list[dict], projects: list[dict], hardware: list[dict]):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_DIR / f"{now.date().isoformat()}-ai-weekly-digest.md"
    all_items = papers + news + projects + hardware
    trend_terms = []
    for term in ["LLM", "agent", "multimodal", "inference", "quantization", "GPU", "TPU", "ASIC", "FPGA", "HBM", "MLPerf"]:
        count = sum(term.lower() in f"{i.get('title', '')} {i.get('summary', '')}".lower() for i in all_items)
        if count:
            trend_terms.append((count, term))
    trends = [term for _, term in sorted(trend_terms, reverse=True)[:8]]
    lines = ["# Weekly AI / AI Accelerator Digest", "", f"日期：{now.date().isoformat()}", "範圍：過去 7 天（Asia/Taipei）", "", "## Executive Summary", ""]
    if trends:
        lines.extend(f"- **{term}** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。" for term in trends[:6])
    else:
        lines.append("- 本週未能從已設定來源取得符合條件的新項目；請檢查網路連線或來源狀態。")

    lines += ["", "## 1. Top AI Papers This Week", ""]
    for item in papers:
        lines += [f"### [{item['title']}]({item['link']})", "", f"- **Authors:** {', '.join(item.get('authors', [])) or 'Unknown'}", f"- **Source:** {item['source']}", f"- **Date:** {_date(item)}", f"- **One-sentence summary:** {summarize(item, 'the contribution and result')}", f"- **Why it matters:** {summarize(item, 'practical research impact')}", f"- **Tags:** {', '.join(item.get('tags', [])) or 'AI/ML'}", ""]
    lines += ["## 2. Industry News", ""]
    for item in news:
        lines += [f"### [{item['title']}]({item['link']})", "", f"- **Source:** {item['source']}", f"- **Date:** {_date(item)}", f"- **Summary:** {summarize(item, 'the announcement')}", f"- **Impact:** {summarize(item, 'industry impact')}", ""]
    lines += ["## 3. Open Source Projects", ""]
    for item in projects:
        lines += [f"### [{item['title']}]({item['link']})", "", f"- **Stars:** {item.get('stars', 0):,}", f"- **Language:** {item.get('language', 'N/A')}", f"- **Updated date:** {_date(item)}", f"- **Summary:** {summarize(item, 'what the project does')}", f"- **Why it is useful:** {summarize(item, 'developer usefulness')}", ""]
    lines += ["## 4. AI Accelerator & Hardware Trends", ""]
    for item in hardware:
        lines += [f"### [{item['title']}]({item['link']})", "", f"- **Source:** {item['source']}", f"- **Date:** {_date(item)}", f"- **Summary:** {summarize(item, 'the main technical development')}", f"- **Hardware relevance:** {summarize(item, 'accelerator architecture, performance, or deployment relevance')}", f"- **Keywords:** {', '.join(_keywords(item)) or 'AI accelerator'}", ""]
    study = trends[:2] + ["FPGA / ASIC accelerator architecture", "systolic arrays and dataflow", "quantized inference optimization"]
    lines += ["## 5. What I Should Study Next", ""] + [f"- {topic}" for topic in dict.fromkeys(study[:5])]
    lines += ["", "## 6. Suggested Reading Order", "", "1. 先讀 Industry News，建立本週產業背景。", "2. 接著瀏覽 Open Source Projects，動手理解工具與工作流。", "3. 再讀 Top AI Papers，掌握方法、實驗與 benchmark。", "4. 最後深入 AI Accelerator & Hardware Trends，串連架構、效能與系統限制。", ""]
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path

