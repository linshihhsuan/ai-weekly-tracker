# Weekly AI / AI Accelerator Digest

日期：2026-09-06
範圍：過去 7 天（Asia/Taipei）

## Executive Summary

- **agent** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **LLM** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **inference** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **multimodal** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **TPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **quantization** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。

## 1. Top AI Papers This Week

### [Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video Understanding](https://arxiv.org/abs/2609.04131v1)

- **Authors:** Hongyu Qu, Guangming Yao, Ling Xing, Xiaobin Hu, Rongxing Ding, Guibin Zhang, Fan Zhang, Yi Yuan, Xiangbo Shu, Shuicheng Yan
- **Source:** arXiv
- **Date:** 2026-09-04
- **One-sentence summary:** Streaming video understanding requires multimodal large language models (MLLMs) to process continuous visual inputs and respond to user queries under strict causality and bounded memory. Existing approaches typically compress historical observations into an external memory bank and retrieve query-relevant evidence as…
- **Why it matters:** Streaming video understanding requires multimodal large language models (MLLMs) to process continuous visual inputs and respond to user queries under strict causality and bounded memory. Existing approaches typically compress historical observations into an external memory bank and retrieve query-relevant evidence as…
- **Tags:** cs.CV

### [Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM](https://arxiv.org/abs/2609.04098v1)

- **Authors:** Sergii Kozyrev, Davyd Maiboroda
- **Source:** arXiv
- **Date:** 2026-09-04
- **One-sentence summary:** Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet (GDN), whose recurrent state summarizes the context in fixed size. Early community 4-bit quantizations of Qwen3.8-27B (48 GDN layers, 16 attention layers) left the GDN block in 8- or 16-bit precision -- especially its decay and writ…
- **Why it matters:** Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet (GDN), whose recurrent state summarizes the context in fixed size. Early community 4-bit quantizations of Qwen3.8-27B (48 GDN layers, 16 attention layers) left the GDN block in 8- or 16-bit precision -- especially its decay and writ…
- **Tags:** cs.AI

### [Para-Pipe: Exploiting Hierarchical Operator Parallelism of ML Computational Graphs on SoCs](https://arxiv.org/abs/2609.04168v1)

- **Authors:** Yujie Zhang, Huiying Lan, Ehsan Aghapour, Zhiyuan Ning, Peng Zan, Weidong Shao, Anuj Pathania, Tulika Mitra
- **Source:** arXiv
- **Date:** 2026-09-04
- **One-sentence summary:** As edge-based deep learning applications become more complex, optimizing performance on heterogeneous System-on-Chips (SoCs) presents unique challenges. Traditional pipelining techniques distributing the computation across different on-chip processing units, while effective for throughput, do not address the latency d…
- **Why it matters:** As edge-based deep learning applications become more complex, optimizing performance on heterogeneous System-on-Chips (SoCs) presents unique challenges. Traditional pipelining techniques distributing the computation across different on-chip processing units, while effective for throughput, do not address the latency d…
- **Tags:** cs.DC, cs.LG, cs.PF

### [Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.04070v1)

- **Authors:** Ruoyu Yao, Yusen Xie, Qingzhao Liu, Pei Liu, Zewei Yang, Yipeng Zhu, Xiaolong Wang, Jun Ma
- **Source:** arXiv
- **Date:** 2026-09-04
- **One-sentence summary:** Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground seman…
- **Why it matters:** Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground seman…
- **Tags:** cs.CV, cs.RO

### [LLM4CKD: Large Language Models for Early Stage Chronic Kidney Disease Screening](https://arxiv.org/abs/2609.04013v1)

- **Authors:** Muhammad Ashad Kabir, Sirajam Munira
- **Source:** arXiv
- **Date:** 2026-09-03
- **One-sentence summary:** Early screening of chronic kidney disease (CKD) is critical for timely intervention, yet most machine learning (ML) and deep learning (DL) approaches require labeled data and model training, limiting their use in real-world screening settings. This study evaluates the effectiveness of large language models (LLMs) for…
- **Why it matters:** Early screening of chronic kidney disease (CKD) is critical for timely intervention, yet most machine learning (ML) and deep learning (DL) approaches require labeled data and model training, limiting their use in real-world screening settings. This study evaluates the effectiveness of large language models (LLMs) for…
- **Tags:** cs.AI, cs.LG

### [Investigating the Ability of Large Language Models to Analyze Recipes for Diabetes](https://arxiv.org/abs/2609.03967v1)

- **Authors:** Revathy Venkataramanan, Aditya Luthra, Venkatesan Nadimuthu, Amit Sheth
- **Source:** arXiv
- **Date:** 2026-09-03
- **One-sentence summary:** Several studies have evaluated the ability of Large Language Models (LLMs) for meal planning, yielding positive outcomes. These models can process natural language inputs and leverage learned knowledge from their pretraining to generate meal plans.
- **Why it matters:** Several studies have evaluated the ability of Large Language Models (LLMs) for meal planning, yielding positive outcomes. These models can process natural language inputs and leverage learned knowledge from their pretraining to generate meal plans.
- **Tags:** cs.CL, cs.AI

### [RATL: Learning from Retrieved Residuals for Robust Multivariate Time-Series Forecasting](https://arxiv.org/abs/2609.03937v1)

- **Authors:** Yuchen He, Yueyang Cang, Zhiyuan Ning, Ningyu Wang, Li Shi
- **Source:** arXiv
- **Date:** 2026-09-03
- **One-sentence summary:** Retrieval-augmented generation (RAG) complements parametric models with retrieved external evidence. The same idea is attractive for continuous-output regression, but directly reusing retrieved target values is often not robust when samples differ in output level, numerical scale, or local dynamics.
- **Why it matters:** Retrieval-augmented generation (RAG) complements parametric models with retrieved external evidence. The same idea is attractive for continuous-output regression, but directly reusing retrieved target values is often not robust when samples differ in output level, numerical scale, or local dynamics.
- **Tags:** cs.LG, cs.AI

### [PatchBench: Evaluating AI Agents for Vulnerability Patching](https://arxiv.org/abs/2609.04075v1)

- **Authors:** Chihao Shen, Jiacheng Li, Aastha Mahajan, Jeffery Siyuan Tian, Yonghwi Kwon, Yizheng Chen
- **Source:** arXiv
- **Date:** 2026-09-04
- **One-sentence summary:** AI agents have recently demonstrated strong performance in automated vulnerability patching. However, existing evaluations often validate a patch only by testing whether the provided Proof-of-Concept (PoC) input still triggers a crash.
- **Why it matters:** AI agents have recently demonstrated strong performance in automated vulnerability patching. However, existing evaluations often validate a patch only by testing whether the provided Proof-of-Concept (PoC) input still triggers a crash.
- **Tags:** cs.CR, cs.AI, cs.SE

## 2. Industry News

### [Building a Memory-Driven Agent with NVIDIA NemoClaw](https://developer.nvidia.com/blog/building-a-memory-driven-agent-with-nvidia-nemoclaw/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-05
- **Summary:** Enterprise work spans messages, decisions, projects, and obligations that change over time. An AI agent that starts without this context must reconstruct it...
- **Impact:** Enterprise work spans messages, decisions, projects, and obligations that change over time. An AI agent that starts without this context must reconstruct it...

### [NVIDIA PAIR Virtual Inference Router Expands Available Compute on Your Local Network](https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-04
- **Summary:** AI agents are learning to do more by working together. A lead agent can break a complex task into smaller jobs and assign those jobs to specialized subagents....
- **Impact:** AI agents are learning to do more by working together. A lead agent can break a complex task into smaller jobs and assign those jobs to specialized subagents....

### [Co-Designing AI Models Using Speculative Decoding for Faster LLM Inference](https://developer.nvidia.com/blog/co-designing-ai-models-using-speculative-decoding-for-faster-llm-inference/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-03
- **Summary:** This post is the third in a series on AI model co-design. It explores how to accelerate LLM inference while maintaining accuracy using speculative decoding and...
- **Impact:** This post is the third in a series on AI model co-design. It explores how to accelerate LLM inference while maintaining accuracy using speculative decoding and...

### [NeoMME: an efficient Multimodal-native and Multilingual Encoder](https://huggingface.co/blog/Hcompany/neomme)

- **Source:** Hugging Face Blog
- **Date:** 2026-09-03
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [The Modern CUDA Toolbox in Practice: A Step-by-Step Optimization Walkthrough](https://developer.nvidia.com/blog/the-modern-cuda-toolbox-in-practice-a-step-by-step-optimization-walkthrough/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-03
- **Summary:** NVIDIA CUDA remains the foundation of GPU-accelerated computing, powering everything from scientific simulations to large-scale AI training. But writing...
- **Impact:** NVIDIA CUDA remains the foundation of GPU-accelerated computing, powering everything from scientific simulations to large-scale AI training. But writing...

### [Frontier Reasoning Reaches the Edge: How to Deploy and Optimize Models on NVIDIA Jetson](https://developer.nvidia.com/blog/frontier-reasoning-reaches-the-edge-how-to-deploy-and-optimize-models-on-nvidia-jetson/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-05
- **Summary:** Running reasoning and agentic AI at the edge has been harder than it needs to be. Until recently, models capable of multi-step reasoning were too large to run...
- **Impact:** Running reasoning and agentic AI at the edge has been harder than it needs to be. Until recently, models capable of multi-step reasoning were too large to run...

### [Fine-tuning a 350M Model for Better Structured Outputs in 100 GRPO Steps](https://huggingface.co/blog/grpo-with-trl-ifstruct)

- **Source:** Hugging Face Blog
- **Date:** 2026-09-03
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [BenchMIRT: What are LLM benchmarks actually measuring?](https://huggingface.co/blog/allenai/benchmirt)

- **Source:** Hugging Face Blog
- **Date:** 2026-09-02
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

## 3. Open Source Projects

### [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

- **Stars:** 44,867
- **Language:** Python
- **Updated date:** 2026-09-06
- **Summary:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码
- **Why it is useful:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

### [langgenius/dify](https://github.com/langgenius/dify)

- **Stars:** 154,555
- **Language:** TypeScript
- **Updated date:** 2026-09-06
- **Summary:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.
- **Why it is useful:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.

### [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)

- **Stars:** 69,054
- **Language:** Python
- **Updated date:** 2026-09-06
- **Summary:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.
- **Why it is useful:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.

### [infiniflow/ragflow](https://github.com/infiniflow/ragflow)

- **Stars:** 90,107
- **Language:** Go
- **Updated date:** 2026-09-05
- **Summary:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs
- **Why it is useful:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

### [deepset-ai/haystack](https://github.com/deepset-ai/haystack)

- **Stars:** 26,427
- **Language:** Python
- **Updated date:** 2026-09-05
- **Summary:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.
- **Why it is useful:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.

### [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production)

- **Stars:** 21,416
- **Language:** Jupyter Notebook
- **Updated date:** 2026-09-05
- **Summary:** End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment.
- **Why it is useful:** End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment.

### [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents)

- **Stars:** 24,156
- **Language:** Jupyter Notebook
- **Updated date:** 2026-09-05
- **Summary:** 50+ tutorials and implementations for Generative AI Agent techniques, from basic conversational bots to complex multi-agent systems.
- **Why it is useful:** 50+ tutorials and implementations for Generative AI Agent techniques, from basic conversational bots to complex multi-agent systems.

### [mem0ai/mem0](https://github.com/mem0ai/mem0)

- **Stars:** 64,756
- **Language:** Python
- **Updated date:** 2026-09-05
- **Summary:** The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists.
- **Why it is useful:** The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists.

## 4. AI Accelerator & Hardware Trends

### [Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video Understanding](https://arxiv.org/abs/2609.04131v1)

- **Source:** arXiv
- **Date:** 2026-09-04
- **Summary:** Streaming video understanding requires multimodal large language models (MLLMs) to process continuous visual inputs and respond to user queries under strict causality and bounded memory. Existing approaches typically compress historical observations into an external memory bank and retrieve query-relevant evidence as…
- **Hardware relevance:** Streaming video understanding requires multimodal large language models (MLLMs) to process continuous visual inputs and respond to user queries under strict causality and bounded memory. Existing approaches typically compress historical observations into an external memory bank and retrieve query-relevant evidence as…
- **Keywords:** NPU

### [Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM](https://arxiv.org/abs/2609.04098v1)

- **Source:** arXiv
- **Date:** 2026-09-04
- **Summary:** Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet (GDN), whose recurrent state summarizes the context in fixed size. Early community 4-bit quantizations of Qwen3.8-27B (48 GDN layers, 16 attention layers) left the GDN block in 8- or 16-bit precision -- especially its decay and writ…
- **Hardware relevance:** Hybrid LLMs pair softmax attention with linear-attention layers such as Gated DeltaNet (GDN), whose recurrent state summarizes the context in fixed size. Early community 4-bit quantizations of Qwen3.8-27B (48 GDN layers, 16 attention layers) left the GDN block in 8- or 16-bit precision -- especially its decay and writ…
- **Keywords:** TPU

### [Para-Pipe: Exploiting Hierarchical Operator Parallelism of ML Computational Graphs on SoCs](https://arxiv.org/abs/2609.04168v1)

- **Source:** arXiv
- **Date:** 2026-09-04
- **Summary:** As edge-based deep learning applications become more complex, optimizing performance on heterogeneous System-on-Chips (SoCs) presents unique challenges. Traditional pipelining techniques distributing the computation across different on-chip processing units, while effective for throughput, do not address the latency d…
- **Hardware relevance:** As edge-based deep learning applications become more complex, optimizing performance on heterogeneous System-on-Chips (SoCs) presents unique challenges. Traditional pipelining techniques distributing the computation across different on-chip processing units, while effective for throughput, do not address the latency d…
- **Keywords:** GPU

### [Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.04070v1)

- **Source:** arXiv
- **Date:** 2026-09-04
- **Summary:** Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground seman…
- **Hardware relevance:** Bridging the gap between the discrete reasoning of Vision-Language Models and the continuous, physics-constrained nature of autonomous driving remains a significant challenge. In this work, we introduce LaPla, a unified Vision-Language-Action (VLA) framework featuring latent-aligned planning to seamlessly ground seman…
- **Keywords:** NPU

### [LLM4CKD: Large Language Models for Early Stage Chronic Kidney Disease Screening](https://arxiv.org/abs/2609.04013v1)

- **Source:** arXiv
- **Date:** 2026-09-03
- **Summary:** Early screening of chronic kidney disease (CKD) is critical for timely intervention, yet most machine learning (ML) and deep learning (DL) approaches require labeled data and model training, limiting their use in real-world screening settings. This study evaluates the effectiveness of large language models (LLMs) for…
- **Hardware relevance:** Early screening of chronic kidney disease (CKD) is critical for timely intervention, yet most machine learning (ML) and deep learning (DL) approaches require labeled data and model training, limiting their use in real-world screening settings. This study evaluates the effectiveness of large language models (LLMs) for…
- **Keywords:** NPU

### [Investigating the Ability of Large Language Models to Analyze Recipes for Diabetes](https://arxiv.org/abs/2609.03967v1)

- **Source:** arXiv
- **Date:** 2026-09-03
- **Summary:** Several studies have evaluated the ability of Large Language Models (LLMs) for meal planning, yielding positive outcomes. These models can process natural language inputs and leverage learned knowledge from their pretraining to generate meal plans.
- **Hardware relevance:** Several studies have evaluated the ability of Large Language Models (LLMs) for meal planning, yielding positive outcomes. These models can process natural language inputs and leverage learned knowledge from their pretraining to generate meal plans.
- **Keywords:** NPU

### [RATL: Learning from Retrieved Residuals for Robust Multivariate Time-Series Forecasting](https://arxiv.org/abs/2609.03937v1)

- **Source:** arXiv
- **Date:** 2026-09-03
- **Summary:** Retrieval-augmented generation (RAG) complements parametric models with retrieved external evidence. The same idea is attractive for continuous-output regression, but directly reusing retrieved target values is often not robust when samples differ in output level, numerical scale, or local dynamics.
- **Hardware relevance:** Retrieval-augmented generation (RAG) complements parametric models with retrieved external evidence. The same idea is attractive for continuous-output regression, but directly reusing retrieved target values is often not robust when samples differ in output level, numerical scale, or local dynamics.
- **Keywords:** TPU

### [PatchBench: Evaluating AI Agents for Vulnerability Patching](https://arxiv.org/abs/2609.04075v1)

- **Source:** arXiv
- **Date:** 2026-09-04
- **Summary:** AI agents have recently demonstrated strong performance in automated vulnerability patching. However, existing evaluations often validate a patch only by testing whether the provided Proof-of-Concept (PoC) input still triggers a crash.
- **Hardware relevance:** AI agents have recently demonstrated strong performance in automated vulnerability patching. However, existing evaluations often validate a patch only by testing whether the provided Proof-of-Concept (PoC) input still triggers a crash.
- **Keywords:** NPU

## 5. What I Should Study Next

- agent
- LLM
- FPGA / ASIC accelerator architecture
- systolic arrays and dataflow
- quantized inference optimization

## 6. Suggested Reading Order

1. 先讀 Industry News，建立本週產業背景。
2. 接著瀏覽 Open Source Projects，動手理解工具與工作流。
3. 再讀 Top AI Papers，掌握方法、實驗與 benchmark。
4. 最後深入 AI Accelerator & Hardware Trends，串連架構、效能與系統限制。
