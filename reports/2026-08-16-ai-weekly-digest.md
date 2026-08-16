# Weekly AI / AI Accelerator Digest

日期：2026-08-16
範圍：過去 7 天（Asia/Taipei）

## Executive Summary

- **agent** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **LLM** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **inference** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **TPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **multimodal** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **GPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。

## 1. Top AI Papers This Week

### [AaLLM: An End-to-End Analog Circuit Design Framework from Topology Generation to Sizing Using Large Language Models](https://arxiv.org/abs/2608.13472v1)

- **Authors:** Mohammed Ayman Habib, Rylan Hart, Morteza Fayazi
- **Source:** arXiv
- **Date:** 2026-08-14
- **One-sentence summary:** Analog circuit design is a time-consuming, iterative process in a nonlinear and high-dimensional design space that relies heavily on expert intuition. Among recent developments, LLMs have introduced a promising approach by bringing natural language reasoning to circuit design tasks.
- **Why it matters:** Analog circuit design is a time-consuming, iterative process in a nonlinear and high-dimensional design space that relies heavily on expert intuition. Among recent developments, LLMs have introduced a promising approach by bringing natural language reasoning to circuit design tasks.
- **Tags:** eess.SY, cs.AI

### [Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for LLM Inference](https://arxiv.org/abs/2608.13426v1)

- **Authors:** Zixuan Lan, Yanhong Li, Jiawei Zhou
- **Source:** arXiv
- **Date:** 2026-08-14
- **One-sentence summary:** Transformer-based language models achieve strong performance but incur substantial inference cost due to repeated high-dimensional matrix multiplications. We propose Reduced Matrix Multiplication (RMM), a training-free, input-adaptive inference method that reduces Transformer matrix products by selecting informative s…
- **Why it matters:** Transformer-based language models achieve strong performance but incur substantial inference cost due to repeated high-dimensional matrix multiplications. We propose Reduced Matrix Multiplication (RMM), a training-free, input-adaptive inference method that reduces Transformer matrix products by selecting informative s…
- **Tags:** cs.LG, cs.AI, cs.CL

### [StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems](https://arxiv.org/abs/2608.13317v1)

- **Authors:** Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
- **Source:** arXiv
- **Date:** 2026-08-13
- **One-sentence summary:** Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck.
- **Why it matters:** Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck.
- **Tags:** cs.AI

### [TabSOM: A tabular-to-image encoding method based on self-organizing maps](https://arxiv.org/abs/2608.13513v1)

- **Authors:** David Chushig-Muzo, María Ángeles Rodríguez de Cara, Eva Milara, Francisco J. Lara-Abelenda, Luis Zhinin-Vera, Diego H. Peluffo-Ordóñez
- **Source:** arXiv
- **Date:** 2026-08-14
- **One-sentence summary:** Tabular-to-image methods have emerged as novel approaches to leverage the high predictive performance of convolutional neural networks and vision transformers. They convert tabular data into image representations, mapping each feature at a fixed pixel location derived from a dimensionality-reduction method (e.g., t-SN…
- **Why it matters:** Tabular-to-image methods have emerged as novel approaches to leverage the high predictive performance of convolutional neural networks and vision transformers. They convert tabular data into image representations, mapping each feature at a fixed pixel location derived from a dimensionality-reduction method (e.g., t-SN…
- **Tags:** cs.CV, cs.LG

### [LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles](https://arxiv.org/abs/2608.13450v1)

- **Authors:** Md Wasiul Haque, Sagar Dasgupta, Mizanur Rahman, Md Rayhanur Rahman
- **Source:** arXiv
- **Date:** 2026-08-14
- **One-sentence summary:** Autonomous vehicles depend on large safety-critical software stacks, where weaknesses reachable from adversarial inputs may affect steering, braking, or other control decisions. Static analysis can identify candidate sites, but dynamically confirming exploitability requires executable test artifacts that are difficult…
- **Why it matters:** Autonomous vehicles depend on large safety-critical software stacks, where weaknesses reachable from adversarial inputs may affect steering, braking, or other control decisions. Static analysis can identify candidate sites, but dynamically confirming exploitability requires executable test artifacts that are difficult…
- **Tags:** cs.SE, cs.CR, cs.LG

### [vToken: Token-Level Virtualization for Reclaimable KV Caches](https://arxiv.org/abs/2608.13263v1)

- **Authors:** Yuanhang Gao, Xiangrui Yang, Yuanfeng Chen, Hongjia Chen, Qianru Lv, Wenfei Wu, Dongsheng Li
- **Source:** arXiv
- **Date:** 2026-08-13
- **One-sentence summary:** Large language model serving faces a critical memory bottleneck: the KV cache grows with sequence length and batch size. PagedAttention uses fixed-size memory blocks to reduce allocator-level fragmentation, but recent KV eviction algorithms operate at a token granularity finer than block-level management.
- **Why it matters:** Large language model serving faces a critical memory bottleneck: the KV cache grows with sequence length and batch size. PagedAttention uses fixed-size memory blocks to reduce allocator-level fragmentation, but recent KV eviction algorithms operate at a token granularity finer than block-level management.
- **Tags:** cs.AI, cs.DC, cs.OS

### [Edit2TikZ: A Comprehensive and Challenging Benchmark for Scientific Figure Editing with TikZ](https://arxiv.org/abs/2608.13441v1)

- **Authors:** Zongyun Zhang, Jiacheng Ruan, Xian Gao, Ruizhu Zhou, Lingcheng Meng, Lining Hu, Ting Liu, Yuzhuo Fu
- **Source:** arXiv
- **Date:** 2026-08-14
- **One-sentence summary:** Although multimodal large language models (MLLMs) have shown substantial potential in visual understanding and graphic code generation, editing scientific figures through code presents a greater challenge: a model must jointly recover visual structure, ground the requested change, generate compilable code, and preserv…
- **Why it matters:** Although multimodal large language models (MLLMs) have shown substantial potential in visual understanding and graphic code generation, editing scientific figures through code presents a greater challenge: a model must jointly recover visual structure, ground the requested change, generate compilable code, and preserv…
- **Tags:** cs.CV

### [Sign Language Video Synthesis via Loss-Guided Multi-Expert GANs](https://arxiv.org/abs/2608.13368v1)

- **Authors:** Dingzhan Nong, Zhihao Ren, Ziqi Li, Tim Lo
- **Source:** arXiv
- **Date:** 2026-08-13
- **One-sentence summary:** This preliminary technical report presents a framework for sign language video synthesis using a loss-guided multi-expert Generative Adversarial Network (GAN) to enhance communication for individuals with hearing impairments. Three specialized discriminators -- global, hand, and head -- each guide a corresponding expe…
- **Why it matters:** This preliminary technical report presents a framework for sign language video synthesis using a loss-guided multi-expert Generative Adversarial Network (GAN) to enhance communication for individuals with hearing impairments. Three specialized discriminators -- global, hand, and head -- each guide a corresponding expe…
- **Tags:** cs.CV, cs.AI

## 2. Industry News

### [Record, train, and deploy from one place with Strands Agents, LeRobot, and Hugging Face Storage Buckets](https://huggingface.co/blog/amazon/strands-lerobot-streaming-data-loop)

- **Source:** Hugging Face Blog
- **Date:** 2026-08-14
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [The builder’s guide to GPT‑5.6](https://openai.com/index/builders-guide-to-gpt-5-6)

- **Source:** OpenAI News
- **Date:** 2026-08-13
- **Summary:** Learn how startups use GPT-5.6 to build faster, more cost-efficient AI agents with smarter model selection and new Responses API capabilities.
- **Impact:** Learn how startups use GPT-5.6 to build faster, more cost-efficient AI agents with smarter model selection and new Responses API capabilities.

### [Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed](https://openai.com/index/previewing-ultrafast)

- **Source:** OpenAI News
- **Date:** 2026-08-13
- **Summary:** Preview Ultrafast, a new OpenAI API service tier that runs GPT-5.6 Sol up to 14× faster. Powered by Cerebras, it delivers up to 750 output tokens per second.
- **Impact:** Preview Ultrafast, a new OpenAI API service tier that runs GPT-5.6 Sol up to 14× faster. Powered by Cerebras, it delivers up to 750 output tokens per second.

### [How to Choose Full-Stack Observability for NVIDIA AI Factories](https://developer.nvidia.com/blog/how-to-choose-full-stack-observability-for-nvidia-ai-factories/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-08-13
- **Summary:** AI infrastructure spans multiple layers, from compute and networking to storage, orchestration, and applications. When performance degrades, identifying the...
- **Impact:** AI infrastructure spans multiple layers, from compute and networking to storage, orchestration, and applications. When performance degrades, identifying the...

### [State of Open Models: Summer 2026 Observations](https://huggingface.co/blog/state-of-open-models-summer-2026)

- **Source:** Hugging Face Blog
- **Date:** 2026-08-14
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [Introducing Gemini 3.7 Flash](https://deepmind.google/blog/introducing-gemini-3-7-flash/)

- **Source:** Google DeepMind Blog
- **Date:** 2026-08-14
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [OpenAI appoints Dali Rajic as Chief Revenue Officer](https://openai.com/index/dali-rajic-chief-revenue-officer)

- **Source:** OpenAI News
- **Date:** 2026-08-13
- **Summary:** OpenAI appoints Dali Rajic as Chief Revenue Officer to lead its global revenue organization and help businesses realize the full value of AI.
- **Impact:** OpenAI appoints Dali Rajic as Chief Revenue Officer to lead its global revenue organization and help businesses realize the full value of AI.

### [NVIDIA Nemotron 3.5 Lightning Delivers Fast, Accurate Specialized Task Execution for Long-Running Agents](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-08-11
- **Summary:** Long-running AI agents spend most of their time on high-volume execution: tool calls, result validation, and subagent delegation. Using a frontier reasoning...
- **Impact:** Long-running AI agents spend most of their time on high-volume execution: tool calls, result validation, and subagent delegation. Using a frontier reasoning...

## 3. Open Source Projects

### [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

- **Stars:** 37,620
- **Language:** Python
- **Updated date:** 2026-08-16
- **Summary:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码
- **Why it is useful:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

### [langgenius/dify](https://github.com/langgenius/dify)

- **Stars:** 152,555
- **Language:** TypeScript
- **Updated date:** 2026-08-15
- **Summary:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.
- **Why it is useful:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.

### [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)

- **Stars:** 66,457
- **Language:** Python
- **Updated date:** 2026-08-16
- **Summary:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.
- **Why it is useful:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.

### [deepset-ai/haystack](https://github.com/deepset-ai/haystack)

- **Stars:** 26,218
- **Language:** Python
- **Updated date:** 2026-08-15
- **Summary:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.
- **Why it is useful:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.

### [infiniflow/ragflow](https://github.com/infiniflow/ragflow)

- **Stars:** 88,556
- **Language:** Go
- **Updated date:** 2026-08-16
- **Summary:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs
- **Why it is useful:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

### [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production)

- **Stars:** 21,286
- **Language:** Jupyter Notebook
- **Updated date:** 2026-08-15
- **Summary:** End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment.
- **Why it is useful:** End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment.

### [mem0ai/mem0](https://github.com/mem0ai/mem0)

- **Stars:** 63,333
- **Language:** Python
- **Updated date:** 2026-08-15
- **Summary:** Universal memory layer for AI Agents
- **Why it is useful:** Universal memory layer for AI Agents

### [OpenNMT/CTranslate2](https://github.com/OpenNMT/CTranslate2)

- **Stars:** 4,620
- **Language:** C++
- **Updated date:** 2026-08-16
- **Summary:** Fast inference engine for Transformer models
- **Why it is useful:** Fast inference engine for Transformer models

## 4. AI Accelerator & Hardware Trends

### [AaLLM: An End-to-End Analog Circuit Design Framework from Topology Generation to Sizing Using Large Language Models](https://arxiv.org/abs/2608.13472v1)

- **Source:** arXiv
- **Date:** 2026-08-14
- **Summary:** Analog circuit design is a time-consuming, iterative process in a nonlinear and high-dimensional design space that relies heavily on expert intuition. Among recent developments, LLMs have introduced a promising approach by bringing natural language reasoning to circuit design tasks.
- **Hardware relevance:** Analog circuit design is a time-consuming, iterative process in a nonlinear and high-dimensional design space that relies heavily on expert intuition. Among recent developments, LLMs have introduced a promising approach by bringing natural language reasoning to circuit design tasks.
- **Keywords:** TPU, NPU

### [Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for LLM Inference](https://arxiv.org/abs/2608.13426v1)

- **Source:** arXiv
- **Date:** 2026-08-14
- **Summary:** Transformer-based language models achieve strong performance but incur substantial inference cost due to repeated high-dimensional matrix multiplications. We propose Reduced Matrix Multiplication (RMM), a training-free, input-adaptive inference method that reduces Transformer matrix products by selecting informative s…
- **Hardware relevance:** Transformer-based language models achieve strong performance but incur substantial inference cost due to repeated high-dimensional matrix multiplications. We propose Reduced Matrix Multiplication (RMM), a training-free, input-adaptive inference method that reduces Transformer matrix products by selecting informative s…
- **Keywords:** NPU

### [StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems](https://arxiv.org/abs/2608.13317v1)

- **Source:** arXiv
- **Date:** 2026-08-13
- **Summary:** Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck.
- **Hardware relevance:** Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck.
- **Keywords:** NPU, ISCA

### [TabSOM: A tabular-to-image encoding method based on self-organizing maps](https://arxiv.org/abs/2608.13513v1)

- **Source:** arXiv
- **Date:** 2026-08-14
- **Summary:** Tabular-to-image methods have emerged as novel approaches to leverage the high predictive performance of convolutional neural networks and vision transformers. They convert tabular data into image representations, mapping each feature at a fixed pixel location derived from a dimensionality-reduction method (e.g., t-SN…
- **Hardware relevance:** Tabular-to-image methods have emerged as novel approaches to leverage the high predictive performance of convolutional neural networks and vision transformers. They convert tabular data into image representations, mapping each feature at a fixed pixel location derived from a dimensionality-reduction method (e.g., t-SN…
- **Keywords:** NPU, ISCA

### [LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles](https://arxiv.org/abs/2608.13450v1)

- **Source:** arXiv
- **Date:** 2026-08-14
- **Summary:** Autonomous vehicles depend on large safety-critical software stacks, where weaknesses reachable from adversarial inputs may affect steering, braking, or other control decisions. Static analysis can identify candidate sites, but dynamically confirming exploitability requires executable test artifacts that are difficult…
- **Hardware relevance:** Autonomous vehicles depend on large safety-critical software stacks, where weaknesses reachable from adversarial inputs may affect steering, braking, or other control decisions. Static analysis can identify candidate sites, but dynamically confirming exploitability requires executable test artifacts that are difficult…
- **Keywords:** TPU, NPU

### [Sign Language Video Synthesis via Loss-Guided Multi-Expert GANs](https://arxiv.org/abs/2608.13368v1)

- **Source:** arXiv
- **Date:** 2026-08-13
- **Summary:** This preliminary technical report presents a framework for sign language video synthesis using a loss-guided multi-expert Generative Adversarial Network (GAN) to enhance communication for individuals with hearing impairments. Three specialized discriminators -- global, hand, and head -- each guide a corresponding expe…
- **Hardware relevance:** This preliminary technical report presents a framework for sign language video synthesis using a loss-guided multi-expert Generative Adversarial Network (GAN) to enhance communication for individuals with hearing impairments. Three specialized discriminators -- global, hand, and head -- each guide a corresponding expe…
- **Keywords:** GPU

### [Reasoning for Social Audio-Visual Question Answering: Where Do We Stand?](https://arxiv.org/abs/2608.13239v1)

- **Source:** arXiv
- **Date:** 2026-08-13
- **Summary:** Training Multimodal Large Language Models for audio-visual social understanding is a crucial step toward embodied social intelligence. Chain-of-thought (CoT) reasoning has become the dominant approach, with HumanOmniV2 and its IntentBench benchmark as a prominent reference point.
- **Hardware relevance:** Training Multimodal Large Language Models for audio-visual social understanding is a crucial step toward embodied social intelligence. Chain-of-thought (CoT) reasoning has become the dominant approach, with HumanOmniV2 and its IntentBench benchmark as a prominent reference point.
- **Keywords:** NPU

### [CoverPrune: Coverage-Driven Token Pruning for 3D VLMs via Optimal Transport](https://arxiv.org/abs/2608.13226v1)

- **Source:** arXiv
- **Date:** 2026-08-13
- **Summary:** While 3D Vision-Language Models (3D VLMs) have demonstrated remarkable spatial reasoning capabilities, they suffer from massive visual token counts that create severe computational bottlenecks during inference. Existing token pruning methods primarily rely on diversity-based selection, discarding similar tokens to max…
- **Hardware relevance:** While 3D Vision-Language Models (3D VLMs) have demonstrated remarkable spatial reasoning capabilities, they suffer from massive visual token counts that create severe computational bottlenecks during inference. Existing token pruning methods primarily rely on diversity-based selection, discarding similar tokens to max…
- **Keywords:** ISCA

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
