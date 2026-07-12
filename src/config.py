"""Central configuration for sources, keywords, and report limits."""
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT_DIR / "reports"
TIMEZONE = ZoneInfo("Asia/Taipei")
LOOKBACK_DAYS = 7
MAX_ITEMS_PER_SECTION = 8
REQUEST_TIMEOUT = 20
USER_AGENT = "ai-weekly-tracker/1.0 (+https://github.com/)"

PAPER_CATEGORIES = ["cs.AI", "cs.LG", "cs.CL", "cs.CV", "stat.ML"]
PAPER_KEYWORDS = [
    "artificial intelligence", "machine learning", "large language model", "LLM",
    "multimodal", "retrieval augmented generation", "RAG", "AI agent",
    "reasoning model", "transformer", "efficient inference", "model compression",
    "quantization", "accelerator", "systolic array", "neural network accelerator",
    "FPGA accelerator", "ASIC accelerator",
]
GITHUB_KEYWORDS = [
    "LLM", "RAG", "AI agent", "inference", "transformer", "CUDA", "Triton",
    "quantization", "vLLM", "llama.cpp", "ml compiler", "ai accelerator",
]
HARDWARE_KEYWORDS = [
    "TPU", "GPU", "NPU", "AI accelerator", "inference accelerator",
    "training accelerator", "systolic array", "compute-in-memory", "HBM",
    "chiplet", "wafer-scale engine", "FPGA AI accelerator", "MLPerf",
    "Hot Chips", "ISSCC", "ISCA", "HPCA", "ASPLOS", "MLSys",
]

# RSS URLs are intentionally centralized so sources can be changed without touching fetch logic.
NEWS_FEEDS = {
    "OpenAI News": "https://openai.com/news/rss.xml",
    "Google DeepMind Blog": "https://deepmind.google/blog/rss.xml",
    "Meta AI Blog": "https://ai.meta.com/blog/rss/",
    "NVIDIA Technical Blog": "https://developer.nvidia.com/blog/feed/",
    "Microsoft AI Blog": "https://blogs.microsoft.com/ai/feed/",
    "Anthropic News": "https://www.anthropic.com/news/rss.xml",
    "Hugging Face Blog": "https://huggingface.co/blog/feed.xml",
}
HARDWARE_FEEDS = {
    "NVIDIA Technical Blog": "https://developer.nvidia.com/blog/feed/",
    "MLCommons": "https://mlcommons.org/feed/",
    "Hot Chips": "https://hotchips.org/feed/",
}

