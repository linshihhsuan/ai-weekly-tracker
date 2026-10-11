# Weekly AI / AI Accelerator Digest

日期：2026-10-11
範圍：過去 7 天（Asia/Taipei）

## Executive Summary

- **LLM** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **agent** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **inference** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **multimodal** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **TPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **GPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。

## 1. Top AI Papers This Week

### [DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception](https://arxiv.org/abs/2610.12266v1)

- **Authors:** Jinghua Hou, Zhe Liu, Hengshuang Zhao
- **Source:** arXiv
- **Date:** 2026-10-09
- **One-sentence summary:** Multimodal large language models have made remarkable progress in bridging vision and language, facilitating various perception tasks essential for human-machine interaction, robotics, and autonomous driving. However, existing MLLM-based perception methods predominantly rely on text-based coordinate representation, wh…
- **Why it matters:** Multimodal large language models have made remarkable progress in bridging vision and language, facilitating various perception tasks essential for human-machine interaction, robotics, and autonomous driving. However, existing MLLM-based perception methods predominantly rely on text-based coordinate representation, wh…
- **Tags:** cs.CV, cs.AI

### [One Block, Multiple Depths: Recurrent Vision Transformers with Depth-Programmed Experts](https://arxiv.org/abs/2610.12448v1)

- **Authors:** Adrian Bulat, Yassine Ouali, Georgios Tzimiropoulos
- **Source:** arXiv
- **Date:** 2026-10-09
- **One-sentence summary:** In this work, we show that a single Transformer block, applied recurrently, can match the accuracy of a full-depth vision encoder at comparable inference FLOPs without intermediate feature distillation. reViT restores depth-specific transformations by representing the FFN at each recurrent depth as a convex combinatio…
- **Why it matters:** In this work, we show that a single Transformer block, applied recurrently, can match the accuracy of a full-depth vision encoder at comparable inference FLOPs without intermediate feature distillation. reViT restores depth-specific transformations by representing the FFN at each recurrent depth as a convex combinatio…
- **Tags:** cs.CV, cs.LG

### [SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference](https://arxiv.org/abs/2610.12327v1)

- **Authors:** Qitong Wang, Xinwei Niu, Mingluo Su, Shanwei Zhao, Shiai Zhu, Huan Wang
- **Source:** arXiv
- **Date:** 2026-10-09
- **One-sentence summary:** The memory-bound nature of the decoding stage of large language model (LLM) inference incurs significant latency. Layer-wise training-free network pruning approaches guided by the Hessian have been a prominent solution to this problem, as pruning reduces the number of nonzero parameters read from memory during decodin…
- **Why it matters:** The memory-bound nature of the decoding stage of large language model (LLM) inference incurs significant latency. Layer-wise training-free network pruning approaches guided by the Hessian have been a prominent solution to this problem, as pruning reduces the number of nonzero parameters read from memory during decodin…
- **Tags:** cs.LG, cs.CL

### [OmniCapBench: A Deep-Structured Evaluation Framework for Fine-Grained Audio-Visual Captioning](https://arxiv.org/abs/2610.12458v1)

- **Authors:** Zhongyu Yang, Jiale Tao, Ruitao Chen, Zuhao Yang, Yingfang Yuan, Xueliang Zhao, Auden, Kai Wang, Shuai Shao, Biao Wang, Steve Yves, Qinglin Lu
- **Source:** arXiv
- **Date:** 2026-10-09
- **One-sentence summary:** Multimodal large language models (MLLMs) are rapidly evolving toward continuous audio--visual reasoning, creating an urgent need for evaluations that expose their capability limits. Audio--visual captioning is an ideal diagnostic task, yet current benchmarks face a coupled trade-off: whole-caption scores provide cover…
- **Why it matters:** Multimodal large language models (MLLMs) are rapidly evolving toward continuous audio--visual reasoning, creating an urgent need for evaluations that expose their capability limits. Audio--visual captioning is an ideal diagnostic task, yet current benchmarks face a coupled trade-off: whole-caption scores provide cover…
- **Tags:** cs.CV

### [Is In-Domain Training Enough for Fine-Grained Industrial Anomaly Understanding?](https://arxiv.org/abs/2610.12310v1)

- **Authors:** Xingwu Zhang, Duanyang Du, Huiling Zhu, Jiayue Dai, Yixiao Liu, Guozhi Liu, Zhihan Zhang, Zijun Long
- **Source:** arXiv
- **Date:** 2026-10-09
- **One-sentence summary:** A single multimodal large language model (MLLM) struggles to excel simultaneously at detection, localization, description, and reasoning in multimodal industrial anomaly understanding (MM-IAU). We show that in-domain training does not close this gap.
- **Why it matters:** A single multimodal large language model (MLLM) struggles to excel simultaneously at detection, localization, description, and reasoning in multimodal industrial anomaly understanding (MM-IAU). We show that in-domain training does not close this gap.
- **Tags:** cs.CV

### [DataSense-Bench: The First Step Toward an AI Scientist](https://arxiv.org/abs/2610.12190v1)

- **Authors:** Yudi Zhang, Mingyu Cao, Lu Yin, Mykola Pechenizkiy, Shiwei Liu
- **Source:** arXiv
- **Date:** 2026-10-08
- **One-sentence summary:** As claims about recursive self-improvement (RSI) and artificial general intelligence (AGI) proliferate, we ask a simple question: do frontier AI models have a sense of data, i.e., can they reliably select the right data for training? We introduce DataSense-Bench to study this capability through the fundamental problem…
- **Why it matters:** As claims about recursive self-improvement (RSI) and artificial general intelligence (AGI) proliferate, we ask a simple question: do frontier AI models have a sense of data, i.e., can they reliably select the right data for training? We introduce DataSense-Bench to study this capability through the fundamental problem…
- **Tags:** cs.LG

### [A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization](https://arxiv.org/abs/2610.12183v1)

- **Authors:** Ming Chen, Rong-Xi Tan, Ke Xue, Yu-Jie Zhou, Taiye Lu, Zhi-Xuan Gao, Peng Xie, Zijun Shen, Chen Lu, Haopu Shang, Chao Qian
- **Source:** arXiv
- **Date:** 2026-10-08
- **One-sentence summary:** Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing grea…
- **Why it matters:** Black-box optimization (BBO) arises in many scientific and engineering problems where objective evaluations are expensive and limited. Recent large language model (LLM) agents offer a new way to approach BBO by combining task semantics, computation, optimization tools, and feedback-driven decision making, showing grea…
- **Tags:** cs.LG, cs.AI, cs.NE

### [GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem Solving](https://arxiv.org/abs/2610.12391v1)

- **Authors:** Jialu Wang, Ruichen Zhang, Xiaoou Liu, Hua Wei, Tianlong Chen
- **Source:** arXiv
- **Date:** 2026-10-09
- **One-sentence summary:** Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and constraints into explicit textual representations for the model to reason over.
- **Why it matters:** Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and constraints into explicit textual representations for the model to reason over.
- **Tags:** cs.AI

## 2. Industry News

### [Impactful scheduling for GPU clusters](https://huggingface.co/blog/allenai/impactful-scheduling)

- **Source:** Hugging Face Blog
- **Date:** 2026-10-09
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [Validate AI Factory Changes with Digital Twins and AI Agents](https://developer.nvidia.com/blog/validate-ai-factory-changes-with-digital-twins-and-ai-agents/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-10-08
- **Summary:** AI factories are some of the most complex operations in the world, combining GPUs, CPUs, switches, DPUs, and SuperNICs alongside schedulers, orchestration...
- **Impact:** AI factories are some of the most complex operations in the world, combining GPUs, CPUs, switches, DPUs, and SuperNICs alongside schedulers, orchestration...

### [Asana cuts model costs 76x in browser tests with GPT-6.1 Sol](https://openai.com/index/asana-browser-agent)

- **Source:** OpenAI News
- **Date:** 2026-10-09
- **Summary:** Using GPT-6 Astra in Codex, Asana made its browser agent 76x cheaper and 5x faster in tests to offer customers more capable models.
- **Impact:** Using GPT-6 Astra in Codex, Asana made its browser agent 76x cheaper and 5x faster in tests to offer customers more capable models.

### [Sophos cuts threat investigation time by 96% with OpenAI Daybreak](https://openai.com/index/sophos)

- **Source:** OpenAI News
- **Date:** 2026-10-09
- **Summary:** Discover how Sophos uses OpenAI’s Daybreak to cut cyber-threat investigation time by 96% and automate 52% of MDR cases while preserving human oversight.
- **Impact:** Discover how Sophos uses OpenAI’s Daybreak to cut cyber-threat investigation time by 96% and automate 52% of MDR cases while preserving human oversight.

### [How Oracle turns days of work into minutes with ChatGPT and Codex](https://openai.com/index/oracle)

- **Source:** OpenAI News
- **Date:** 2026-10-09
- **Summary:** Across recruiting, engineering, and operations, Oracle turns specialist knowledge into fast, repeatable workflows with ChatGPT Work and Codex.
- **Impact:** Across recruiting, engineering, and operations, Oracle turns specialist knowledge into fast, repeatable workflows with ChatGPT Work and Codex.

### [LegalOn halves Codex costs while maintaining development speed](https://openai.com/index/legalon-halves-codex-costs)

- **Source:** OpenAI News
- **Date:** 2026-10-08
- **Summary:** LegalOn cut estimated daily Codex costs by 65% while maintaining development speed. It matched Astra, Sol, and Luna to tasks and managed budgets strategically.
- **Impact:** LegalOn cut estimated daily Codex costs by 65% while maintaining development speed. It matched Astra, Sol, and Luna to tasks and managed budgets strategically.

### [5 Steps to Create SimReady Assets for Robotics with Frontier AI Models](https://developer.nvidia.com/blog/5-steps-to-create-simready-assets-for-robotics-with-frontier-ai-models/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-10-09
- **Summary:** Preparing CAD assets for robotics simulation requires more than converting geometry to OpenUSD: developers must configure and validate materials, collision...
- **Impact:** Preparing CAD assets for robotics simulation requires more than converting geometry to OpenUSD: developers must configure and validate materials, collision...

### [Building Reliable Data Analytics Agents: Lessons from the KDD Cup](https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-10-09
- **Summary:** The NVIDIA KGMON team placed second in the KDD Cup 2026 Data Agents competition with a system built around a simple idea of making an agent's harness smaller,...
- **Impact:** The NVIDIA KGMON team placed second in the KDD Cup 2026 Data Agents competition with a system built around a simple idea of making an agent's harness smaller,...

## 3. Open Source Projects

### [langgenius/dify](https://github.com/langgenius/dify)

- **Stars:** 158,108
- **Language:** TypeScript
- **Updated date:** 2026-10-11
- **Summary:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.
- **Why it is useful:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.

### [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)

- **Stars:** 85,170
- **Language:** Python
- **Updated date:** 2026-10-11
- **Summary:** Open-source web crawler and scraper for LLMs and AI agents: any website into clean, LLM-ready Markdown. Run it yourself, or use Crawl4AI Cloud with one key.
- **Why it is useful:** Open-source web crawler and scraper for LLMs and AI agents: any website into clean, LLM-ready Markdown. Run it yourself, or use Crawl4AI Cloud with one key.

### [deepset-ai/haystack](https://github.com/deepset-ai/haystack)

- **Stars:** 26,715
- **Language:** Python
- **Updated date:** 2026-10-11
- **Summary:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.
- **Why it is useful:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.

### [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)

- **Stars:** 74,976
- **Language:** Python
- **Updated date:** 2026-10-11
- **Summary:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.
- **Why it is useful:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.

### [infiniflow/ragflow](https://github.com/infiniflow/ragflow)

- **Stars:** 91,980
- **Language:** Go
- **Updated date:** 2026-10-11
- **Summary:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs
- **Why it is useful:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

### [OpenNMT/CTranslate2](https://github.com/OpenNMT/CTranslate2)

- **Stars:** 4,703
- **Language:** C++
- **Updated date:** 2026-10-11
- **Summary:** Fast inference engine for Transformer models
- **Why it is useful:** Fast inference engine for Transformer models

### [arc53/DocsGPT](https://github.com/arc53/DocsGPT)

- **Stars:** 18,316
- **Language:** Python
- **Updated date:** 2026-10-11
- **Summary:** Private AI platform for agents, assistants and enterprise search. Built-in Agent Builder, Deep research, Document analysis, Multi-model support, and API connectivity for agents.
- **Why it is useful:** Private AI platform for agents, assistants and enterprise search. Built-in Agent Builder, Deep research, Document analysis, Multi-model support, and API connectivity for agents.

### [Jit-Roy/WeeLLM](https://github.com/Jit-Roy/WeeLLM)

- **Stars:** 86
- **Language:** Python
- **Updated date:** 2026-10-11
- **Summary:** WeeLLM runs large diffusion models with as little as 4 GB of VRAM, without any quantization. It dynamically determines how many layers can fit within the available VRAM and streams the text encoder and transformer layers to the GPU layer by layer, enabling inference on hardware with limited VRAM.
- **Why it is useful:** WeeLLM runs large diffusion models with as little as 4 GB of VRAM, without any quantization. It dynamically determines how many layers can fit within the available VRAM and streams the text encoder and transformer layers to the GPU layer by layer, enabling inference on hardware with limited VRAM.

## 4. AI Accelerator & Hardware Trends

### [DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception](https://arxiv.org/abs/2610.12266v1)

- **Source:** arXiv
- **Date:** 2026-10-09
- **Summary:** Multimodal large language models have made remarkable progress in bridging vision and language, facilitating various perception tasks essential for human-machine interaction, robotics, and autonomous driving. However, existing MLLM-based perception methods predominantly rely on text-based coordinate representation, wh…
- **Hardware relevance:** Multimodal large language models have made remarkable progress in bridging vision and language, facilitating various perception tasks essential for human-machine interaction, robotics, and autonomous driving. However, existing MLLM-based perception methods predominantly rely on text-based coordinate representation, wh…
- **Keywords:** TPU

### [One Block, Multiple Depths: Recurrent Vision Transformers with Depth-Programmed Experts](https://arxiv.org/abs/2610.12448v1)

- **Source:** arXiv
- **Date:** 2026-10-09
- **Summary:** In this work, we show that a single Transformer block, applied recurrently, can match the accuracy of a full-depth vision encoder at comparable inference FLOPs without intermediate feature distillation. reViT restores depth-specific transformations by representing the FFN at each recurrent depth as a convex combinatio…
- **Hardware relevance:** In this work, we show that a single Transformer block, applied recurrently, can match the accuracy of a full-depth vision encoder at comparable inference FLOPs without intermediate feature distillation. reViT restores depth-specific transformations by representing the FFN at each recurrent depth as a convex combinatio…
- **Keywords:** TPU

### [SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference](https://arxiv.org/abs/2610.12327v1)

- **Source:** arXiv
- **Date:** 2026-10-09
- **Summary:** The memory-bound nature of the decoding stage of large language model (LLM) inference incurs significant latency. Layer-wise training-free network pruning approaches guided by the Hessian have been a prominent solution to this problem, as pruning reduces the number of nonzero parameters read from memory during decodin…
- **Hardware relevance:** The memory-bound nature of the decoding stage of large language model (LLM) inference incurs significant latency. Layer-wise training-free network pruning approaches guided by the Hessian have been a prominent solution to this problem, as pruning reduces the number of nonzero parameters read from memory during decodin…
- **Keywords:** GPU

### [GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem Solving](https://arxiv.org/abs/2610.12391v1)

- **Source:** arXiv
- **Date:** 2026-10-09
- **Summary:** Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and constraints into explicit textual representations for the model to reason over.
- **Hardware relevance:** Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and constraints into explicit textual representations for the model to reason over.
- **Keywords:** TPU

### [Long Text to Predictive Features: LLM-Guided Blockwise Feature Engineering via Executable Program Search](https://arxiv.org/abs/2610.12390v1)

- **Source:** arXiv
- **Date:** 2026-10-09
- **Summary:** Industrial risk-control systems typically rely on structured-data models for efficient prediction, yet substantial valuable information remains embedded in unstructured long text. Extracting this information through manual feature engineering is labor-intensive, while requiring a large language model (LLM) to process…
- **Hardware relevance:** Industrial risk-control systems typically rely on structured-data models for efficient prediction, yet substantial valuable information remains embedded in unstructured long text. Extracting this information through manual feature engineering is labor-intensive, while requiring a large language model (LLM) to process…
- **Keywords:** NPU

### [Distilling Routed 3D Privilege for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.12355v1)

- **Source:** arXiv
- **Date:** 2026-10-09
- **Summary:** Spatial reasoning remains a persistent weakness of vision-language models (VLMs), because RGB inputs do not directly provide geometric evidence. Existing remedies either inject 3D into the model at inference, paying architecture and latency costs, or train with outcome rewards that supervise only the final answer.
- **Hardware relevance:** Spatial reasoning remains a persistent weakness of vision-language models (VLMs), because RGB inputs do not directly provide geometric evidence. Existing remedies either inject 3D into the model at inference, paying architecture and latency costs, or train with outcome rewards that supervise only the final answer.
- **Keywords:** NPU

### [SpaceCast-Bench: Evaluating Predictive Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.12402v1)

- **Source:** arXiv
- **Date:** 2026-10-09
- **Summary:** Existing spatial reasoning benchmarks mainly test spatial perception: reading off relations already visible in the input. Yet real-world spatial intelligence demands predictive spatial reasoning: constructing a scene from observations, anticipating how an intervention changes it, and reasoning about the unseen outcome.
- **Hardware relevance:** Existing spatial reasoning benchmarks mainly test spatial perception: reading off relations already visible in the input. Yet real-world spatial intelligence demands predictive spatial reasoning: constructing a scene from observations, anticipating how an intervention changes it, and reasoning about the unseen outcome.
- **Keywords:** NPU

### [Batch Before You Lift: Scalable Topological Deep Learning on Large Graphs](https://arxiv.org/abs/2610.12247v1)

- **Source:** arXiv
- **Date:** 2026-10-09
- **Summary:** Topological Deep Learning extends graph-based learning to higher-order domains, such as hypergraphs, cellular, and simplicial complexes. These domains are typically constructed from patterns in an input graph through a process of graph lifting.
- **Hardware relevance:** Topological Deep Learning extends graph-based learning to higher-order domains, such as hypergraphs, cellular, and simplicial complexes. These domains are typically constructed from patterns in an input graph through a process of graph lifting.
- **Keywords:** GPU, NPU

## 5. What I Should Study Next

- LLM
- agent
- FPGA / ASIC accelerator architecture
- systolic arrays and dataflow
- quantized inference optimization

## 6. Suggested Reading Order

1. 先讀 Industry News，建立本週產業背景。
2. 接著瀏覽 Open Source Projects，動手理解工具與工作流。
3. 再讀 Top AI Papers，掌握方法、實驗與 benchmark。
4. 最後深入 AI Accelerator & Hardware Trends，串連架構、效能與系統限制。
