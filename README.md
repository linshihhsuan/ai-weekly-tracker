# AI Weekly Tracker

自動蒐集過去 7 天的 AI 論文、模型公司新聞、熱門開源專案，以及 AI accelerator／GPU／TPU／ASIC／FPGA 等硬體趨勢，並產生適合循序閱讀的 Markdown 週報。日期、週期與報告檔名皆以 **Asia/Taipei** 為準。

## 功能

- arXiv：追蹤 `cs.AI`、`cs.LG`、`cs.CL`、`cs.CV`、`stat.ML`。
- 產業 RSS：OpenAI、Google DeepMind、Meta AI、NVIDIA、Microsoft AI、Anthropic、Hugging Face。
- GitHub Search API：有 token 時提高額度；無 token 時採少量公開請求。
- 硬體：MLPerf、NVIDIA 與研討會／架構關鍵字，並從論文和新聞交叉篩選。
- 可維護的透明評分：新鮮度、關鍵字、硬體／推論訊號、GitHub stars 與更新日期。
- 單一來源失效不會中止，其餘資料仍會形成報告；URL／標題會去重。
- 無 OpenAI key 時使用 extractive summary；有 key 時使用較自然的一句摘要。

## 安裝

需要 Python 3.11+：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

macOS／Linux 啟用環境可使用 `source .venv/bin/activate`，複製設定則使用 `cp .env.example .env`。

## 設定 `.env`

```dotenv
OPENAI_API_KEY=
GITHUB_TOKEN=
```

兩者都可留空。`OPENAI_API_KEY` 啟用自然語言摘要；`GITHUB_TOKEN` 提升 GitHub API rate limit。請勿提交 `.env`，也不要把 key 寫進程式碼。若要在 Actions 使用，請在 repository 的 **Settings → Secrets and variables → Actions** 建立同名 secrets。

## 本機執行

```powershell
python src/main.py
```

輸出位於 `reports/YYYY-MM-DD-ai-weekly-digest.md`。網路來源偶爾會更換 RSS URL；警告會記錄失敗來源，但不影響其他來源。

## GitHub Actions 排程

`.github/workflows/weekly_ai_digest.yml` 會在每週日 `01:00 UTC`（台北時間 `09:00`）執行，也可從 Actions 頁面按 **Run workflow**。Workflow 需要 `contents: write` 權限才能 commit 報告；若組織政策關閉寫入，請在 repository Actions 設定允許 read/write permissions。

## 修改來源與關鍵字

集中修改 `src/config.py`：

- `NEWS_FEEDS`、`HARDWARE_FEEDS`：RSS/Atom 來源。
- `PAPER_CATEGORIES`、`PAPER_KEYWORDS`：arXiv 分類與搜尋字詞。
- `GITHUB_KEYWORDS`、`HARDWARE_KEYWORDS`：開源及硬體關鍵字。
- `LOOKBACK_DAYS`、`MAX_ITEMS_PER_SECTION`：時間範圍與每區筆數。

評分權重位於 `src/rank_items.py`，每一項計分都有簡短註解，可依閱讀偏好調整。

## 報告範例

```markdown
# Weekly AI / AI Accelerator Digest
日期：2026-07-12
範圍：過去 7 天（Asia/Taipei）

## 1. Top AI Papers This Week
### [Example paper](https://arxiv.org/abs/xxxx.xxxxx)
- **Authors:** A. Author
- **Why it matters:** Improves inference throughput with lower memory use.
```

## 常見問題

- **GitHub 403 / rate limit**：設定 `GITHUB_TOKEN`；無 token 模式刻意只發送少量請求。
- **某區塊沒有資料**：可能是近 7 天沒有匹配項目、RSS 暫時失效或來源封鎖請求；查看終端 warning。
- **OpenAI 摘要失敗**：程式會自動回退至 extractive summary。也可不設定 key。
- **Actions 無法 push**：確認 workflow permissions 為 read/write，且分支保護允許 GitHub Actions 寫入。
- **時區日期不符**：不要改 cron 的註解當作時區設定；程式內日期由 `ZoneInfo("Asia/Taipei")` 計算。

## 安全性

程式只從環境變數讀取 API key/token，不會將它們寫入報告或原始碼。請將本機 `.env` 排除於版本控制。

