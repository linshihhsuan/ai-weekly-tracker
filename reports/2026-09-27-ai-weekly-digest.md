# Weekly AI / AI Accelerator Digest

日期：2026-09-27
範圍：過去 7 天（Asia/Taipei）

## Executive Summary

- **agent** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **LLM** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **inference** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **TPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **GPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **multimodal** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。

## 1. Top AI Papers This Week

### [Mind What Matters for Reasoning: Aligning Cross-Modal Attention via Selective Probability Mass Concentration](https://arxiv.org/abs/2609.29940v1)

- **Authors:** Jiaqi Deng, Zonghan Wu, Zhan Heng, Xiaoshui Huang, Huan Huo, Guandong Xu
- **Source:** arXiv
- **Date:** 2026-09-24
- **One-sentence summary:** Multimodal large language models (MLLMs) achieve strong performance on visual reasoning tasks, yet remain prone to hallucinations and over-reliance on language priors, often generating answers without adequately using task-relevant visual evidence. Existing approaches primarily improve reasoning through reasoning-orie…
- **Why it matters:** Multimodal large language models (MLLMs) achieve strong performance on visual reasoning tasks, yet remain prone to hallucinations and over-reliance on language priors, often generating answers without adequately using task-relevant visual evidence. Existing approaches primarily improve reasoning through reasoning-orie…
- **Tags:** cs.CV, cs.AI

### [KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization](https://arxiv.org/abs/2609.30059v1)

- **Authors:** Aheli Poddar, Sanskar Prasad, Arindam Samanta, Subha Chakraborty, Vishal Goyal, Rohit Singh Rathaur
- **Source:** arXiv
- **Date:** 2026-09-25
- **One-sentence summary:** Deep learning inference and training performance depends critically on GPU kernel efficiency. Modern compilers such as PyTorch Inductor automatically generate GPU kernels from high-level model code, but frequently underperform expert-written implementations by wide margins.
- **Why it matters:** Deep learning inference and training performance depends critically on GPU kernel efficiency. Modern compilers such as PyTorch Inductor automatically generate GPU kernels from high-level model code, but frequently underperform expert-written implementations by wide margins.
- **Tags:** cs.DC, cs.AI, cs.LG

### [Screen Before You Serve: Simulation for Production Customer Experience AI Agents at 140M Scale](https://arxiv.org/abs/2609.30137v1)

- **Authors:** Edesio Alcoba, Kevin Rossell, Aman Gupta, Shao Tang, Jiwoo Hong, Pabel Carrillo-Mendoza, Wanderson Conceição Ferreira, Alvaro Tedeschi, Zayd Simjee, Shreya Rajpal, Bruno Finardi Hime, Christian Sousa, Luis Moneda, Herbert Fei, Daniel Silva, Rohan Ramanath
- **Source:** arXiv
- **Date:** 2026-09-25
- **One-sentence summary:** Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especially in regulated industries, is difficult: they must detect intent, follow complex operational policies and use tools re…
- **Why it matters:** Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especially in regulated industries, is difficult: they must detect intent, follow complex operational policies and use tools re…
- **Tags:** cs.AI, cs.CL

### [How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt Structure](https://arxiv.org/abs/2609.30074v1)

- **Authors:** Dipankar Sarkar
- **Source:** arXiv
- **Date:** 2026-09-25
- **One-sentence summary:** Evaluations of LLM systems routinely average over small prompt sets and report models as a ranked table. We ask how much confidence such a table deserves, using LLM-based prompt-structure inference as the case study: eight open model variants across five families and 8B to 675B parameters, caching disabled, 293 raw in…
- **Why it matters:** Evaluations of LLM systems routinely average over small prompt sets and report models as a ranked table. We ask how much confidence such a table deserves, using LLM-based prompt-structure inference as the case study: eight open model variants across five families and 8B to 675B parameters, caching disabled, 293 raw in…
- **Tags:** cs.CL, cs.AI, cs.LG

### [Residual Correlation as a Diagnostic for Joint-Uncertainty Gains from GP Coregionalisation](https://arxiv.org/abs/2609.30085v1)

- **Authors:** Fangqin Zhou, Joaquin Vanschoren
- **Source:** arXiv
- **Date:** 2026-09-25
- **One-sentence summary:** In multi-target regression, correlated targets are often coupled through multi-output Gaussian processes with an intrinsic model of coregionalisation (GP-ICM), assuming that sharing statistical strength improves overall performance. In practice, the benefits are inconsistent.
- **Why it matters:** In multi-target regression, correlated targets are often coupled through multi-output Gaussian processes with an intrinsic model of coregionalisation (GP-ICM), assuming that sharing statistical strength improves overall performance. In practice, the benefits are inconsistent.
- **Tags:** cs.LG

### [MILO: Efficient Many-shot In-Context Learning with Block-wise Low-rank Compression](https://arxiv.org/abs/2609.29913v1)

- **Authors:** Youpeng Zhao, Tian Tan, Liqian Peng, Jun Wang, Alec Go
- **Source:** arXiv
- **Date:** 2026-09-24
- **One-sentence summary:** Many-shot in-context learning (ICL) enables large language models (LLMs) to adapt to complex tasks by conditioning on thousands of demonstration examples, but this paradigm shifts the inference efficiency bottleneck to the key-value (KV) cache memory. Due to the linear scaling behavior of the KV cache, storing these i…
- **Why it matters:** Many-shot in-context learning (ICL) enables large language models (LLMs) to adapt to complex tasks by conditioning on thousands of demonstration examples, but this paradigm shifts the inference efficiency bottleneck to the key-value (KV) cache memory. Due to the linear scaling behavior of the KV cache, storing these i…
- **Tags:** cs.CL

### [Towards Practical Compression of 3D Gaussian Splatting](https://arxiv.org/abs/2609.30245v1)

- **Authors:** Pengpeng Yu, Yueru Chen, Fei Song, Tai Qin, Qi Zhang, Jing Wang, Yulan Guo
- **Source:** arXiv
- **Date:** 2026-09-25
- **One-sentence summary:** 3D Gaussian Splatting (3DGS) enables high-quality novel-view synthesis but requires substantial storage. Existing compression methods often rely on spatial context modeling over irregular 3D representations, increasing the complexity of training and coding.
- **Why it matters:** 3D Gaussian Splatting (3DGS) enables high-quality novel-view synthesis but requires substantial storage. Existing compression methods often rely on spatial context modeling over irregular 3D representations, increasing the complexity of training and coding.
- **Tags:** cs.CV

### [Coding Agents for Generalized Task and Motion Planning Problems](https://arxiv.org/abs/2609.30233v1)

- **Authors:** Matteo Merler, Bowen Li, Josh Roy, Yichao Liang, Qianwei Wang, Yixuan Huang, Tom Silver
- **Source:** arXiv
- **Date:** 2026-09-25
- **One-sentence summary:** Task and motion planning (TAMP) problems remain difficult even with full observability and object-centric states because discrete decisions are tightly coupled to geometric, kinematic, and dynamic constraints. Generalized TAMP addresses this difficulty by exploiting regularities across problem instances to reduce plan…
- **Why it matters:** Task and motion planning (TAMP) problems remain difficult even with full observability and object-centric states because discrete decisions are tightly coupled to geometric, kinematic, and dynamic constraints. Generalized TAMP addresses this difficulty by exploiting regularities across problem instances to reduce plan…
- **Tags:** cs.RO, cs.AI

## 2. Industry News

### [Proaction boosts sales 60% and saves 75+ hours with Codex](https://openai.com/index/proaction)

- **Source:** OpenAI News
- **Date:** 2026-09-26
- **Summary:** With Codex, GPT-Live-1, and GPT-6 Astra, Proaction builds, operates, and sells modern fleet management faster.
- **Impact:** With Codex, GPT-Live-1, and GPT-6 Astra, Proaction builds, operates, and sells modern fleet management faster.

### [Efficient MoE Training for Biological Foundation Models](https://developer.nvidia.com/blog/efficient-moe-training-for-biological-foundation-models/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-24
- **Summary:** As language models grow, scaling dense architectures becomes increasingly expensive. In a dense transformer, every token passes through every layer, so adding...
- **Impact:** As language models grow, scaling dense architectures becomes increasingly expensive. In a dense transformer, every token passes through every layer, so adding...

### [Accelerating a ROS 2 Node with an AI Agent and NVIDIA Isaac ROS](https://developer.nvidia.com/blog/accelerating-a-ros-2-node-with-an-ai-agent-and-nvidia-isaac-ros/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-22
- **Summary:** GPU acceleration can speed up compute-intensive robotics workloads, but a fast CUDA kernel alone does not guarantee a fast ROS 2 graph. As messages move between...
- **Impact:** GPU acceleration can speed up compute-intensive robotics workloads, but a fast CUDA kernel alone does not guarantee a fast ROS 2 graph. As messages move between...

### [Enabling Private High-Performance Production AI Inference with NVIDIA Confidential Computing](https://developer.nvidia.com/blog/enabling-private-high-performance-production-ai-inference-with-nvidia-confidential-computing/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-23
- **Summary:** As large language model (LLM) inference increasingly processes sensitive information and proprietary model context across personal, enterprise, and regulated...
- **Impact:** As large language model (LLM) inference increasingly processes sensitive information and proprietary model context across personal, enterprise, and regulated...

### [Manage Kubernetes Node Fleets with NodeWright](https://developer.nvidia.com/blog/manage-kubernetes-node-fleets-with-nodewright/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-24
- **Summary:** Kubernetes manages what runs on your nodes. Managing the nodes themselves is the challenge: kernel settings, system packages, storage layouts, security agents,...
- **Impact:** Kubernetes manages what runs on your nodes. Managing the nodes themselves is the challenge: kernel settings, system packages, storage layouts, security agents,...

### [Ringg’s AI agents resolve up to 65% of customer calls with OpenAI](https://openai.com/index/ringg)

- **Source:** OpenAI News
- **Date:** 2026-09-23
- **Summary:** Using GPT-5.6, Ringg powers multilingual agents across voice, chat, WhatsApp, and web for 90% less cost vs. GPT-4.1.
- **Impact:** Using GPT-5.6, Ringg powers multilingual agents across voice, chat, WhatsApp, and web for 90% less cost vs. GPT-4.1.

### [Validate GPU Cluster Readiness Before AI Workloads Land](https://developer.nvidia.com/blog/validate-gpu-cluster-readiness-before-ai-workloads-land/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-24
- **Summary:** A GPU cluster can pass every health check and still fail to run an AI workload. Even when every GPU, network link, and pod reports healthy, a 512-GPU training...
- **Impact:** A GPU cluster can pass every health check and still fail to run an AI workload. Even when every GPU, network link, and pod reports healthy, a 512-GPU training...

### [Simplifying Model Serving Across Multiple GPUs with NVIDIA TensorRT Multi-Device Integration in NVIDIA Dynamo-Triton](https://developer.nvidia.com/blog/simplifying-model-serving-across-multiple-gpus-with-nvidia-tensorrt-multi-device-integration-in-nvidia-dynamo-triton/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-09-22
- **Summary:** The compute and memory demands of generative AI increasingly exceed what a single GPU can provide. NVIDIA TensorRT multi-device inference is a new capability...
- **Impact:** The compute and memory demands of generative AI increasingly exceed what a single GPU can provide. NVIDIA TensorRT multi-device inference is a new capability...

## 3. Open Source Projects

### [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

- **Stars:** 51,216
- **Language:** Python
- **Updated date:** 2026-09-27
- **Summary:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码
- **Why it is useful:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

### [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)

- **Stars:** 73,900
- **Language:** Python
- **Updated date:** 2026-09-27
- **Summary:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.
- **Why it is useful:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.

### [langgenius/dify](https://github.com/langgenius/dify)

- **Stars:** 157,301
- **Language:** TypeScript
- **Updated date:** 2026-09-27
- **Summary:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.
- **Why it is useful:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.

### [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)

- **Stars:** 66,509
- **Language:** JavaScript
- **Updated date:** 2026-09-26
- **Summary:** Stop renting your intelligence. Own it with AnythingLLM.
- **Why it is useful:** Stop renting your intelligence. Own it with AnythingLLM.

### [cactus-compute/cactus](https://github.com/cactus-compute/cactus)

- **Stars:** 6,068
- **Language:** C++
- **Updated date:** 2026-09-26
- **Summary:** Quantization, kernels, runtime and inference engine for mobiles, wearables, smart home and robots.
- **Why it is useful:** Quantization, kernels, runtime and inference engine for mobiles, wearables, smart home and robots.

### [deepset-ai/haystack](https://github.com/deepset-ai/haystack)

- **Stars:** 26,611
- **Language:** Python
- **Updated date:** 2026-09-26
- **Summary:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.
- **Why it is useful:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.

### [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

- **Stars:** 139,908
- **Language:** Python
- **Updated date:** 2026-09-26
- **Summary:** 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- **Why it is useful:** 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.

### [infiniflow/ragflow](https://github.com/infiniflow/ragflow)

- **Stars:** 91,337
- **Language:** Go
- **Updated date:** 2026-09-26
- **Summary:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs
- **Why it is useful:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

## 4. AI Accelerator & Hardware Trends

### [KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization](https://arxiv.org/abs/2609.30059v1)

- **Source:** arXiv
- **Date:** 2026-09-25
- **Summary:** Deep learning inference and training performance depends critically on GPU kernel efficiency. Modern compilers such as PyTorch Inductor automatically generate GPU kernels from high-level model code, but frequently underperform expert-written implementations by wide margins.
- **Hardware relevance:** Deep learning inference and training performance depends critically on GPU kernel efficiency. Modern compilers such as PyTorch Inductor automatically generate GPU kernels from high-level model code, but frequently underperform expert-written implementations by wide margins.
- **Keywords:** GPU

### [Screen Before You Serve: Simulation for Production Customer Experience AI Agents at 140M Scale](https://arxiv.org/abs/2609.30137v1)

- **Source:** arXiv
- **Date:** 2026-09-25
- **Summary:** Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especially in regulated industries, is difficult: they must detect intent, follow complex operational policies and use tools re…
- **Hardware relevance:** Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especially in regulated industries, is difficult: they must detect intent, follow complex operational policies and use tools re…
- **Keywords:** TPU

### [How Reproducible Are Evaluation Conclusions? A Self-Audit of LLM-Inferred Prompt Structure](https://arxiv.org/abs/2609.30074v1)

- **Source:** arXiv
- **Date:** 2026-09-25
- **Summary:** Evaluations of LLM systems routinely average over small prompt sets and report models as a ranked table. We ask how much confidence such a table deserves, using LLM-based prompt-structure inference as the case study: eight open model variants across five families and 8B to 675B parameters, caching disabled, 293 raw in…
- **Hardware relevance:** Evaluations of LLM systems routinely average over small prompt sets and report models as a ranked table. We ask how much confidence such a table deserves, using LLM-based prompt-structure inference as the case study: eight open model variants across five families and 8B to 675B parameters, caching disabled, 293 raw in…
- **Keywords:** TPU

### [Residual Correlation as a Diagnostic for Joint-Uncertainty Gains from GP Coregionalisation](https://arxiv.org/abs/2609.30085v1)

- **Source:** arXiv
- **Date:** 2026-09-25
- **Summary:** In multi-target regression, correlated targets are often coupled through multi-output Gaussian processes with an intrinsic model of coregionalisation (GP-ICM), assuming that sharing statistical strength improves overall performance. In practice, the benefits are inconsistent.
- **Hardware relevance:** In multi-target regression, correlated targets are often coupled through multi-output Gaussian processes with an intrinsic model of coregionalisation (GP-ICM), assuming that sharing statistical strength improves overall performance. In practice, the benefits are inconsistent.
- **Keywords:** TPU

### [The Alignment Illusion in Multimodal Large Language Models](https://arxiv.org/abs/2609.30210v1)

- **Source:** arXiv
- **Date:** 2026-09-25
- **Summary:** Layer-wise visual-text similarity in Multimodal Large Language Models (MLLMs) is widely interpreted as evidence that the language model progressively integrates visual content into a shared representation space. This reading rests on the assumption that scalar alignment scores reflect content-level cross-modal interac…
- **Hardware relevance:** Layer-wise visual-text similarity in Multimodal Large Language Models (MLLMs) is widely interpreted as evidence that the language model progressively integrates visual content into a shared representation space. This reading rests on the assumption that scalar alignment scores reflect content-level cross-modal interac…
- **Keywords:** TPU

### [Accelerating Video Diffusion via Training-Free Trajectory Routing](https://arxiv.org/abs/2609.30096v1)

- **Source:** arXiv
- **Date:** 2026-09-25
- **Summary:** Video diffusion is computationally expensive, as it requires executing a large model across many denoising steps. Even with step-distillation, inference remains expensive because every distilled step still requires a costly model evaluation.
- **Hardware relevance:** Video diffusion is computationally expensive, as it requires executing a large model across many denoising steps. Even with step-distillation, inference remains expensive because every distilled step still requires a costly model evaluation.
- **Keywords:** NPU

### [Neuro-symbolic AI for Industrial Configuration](https://arxiv.org/abs/2609.29947v1)

- **Source:** arXiv
- **Date:** 2026-09-24
- **Summary:** Large Language Models (LLMs) have shown impressive performance on a wide range of generative tasks. Yet their probabilistic nature makes them, in isolation, fundamentally unsuited for industrial product configuration, where outputs must be syntactically valid, semantically consistent with a knowledge base of hundreds…
- **Hardware relevance:** Large Language Models (LLMs) have shown impressive performance on a wide range of generative tasks. Yet their probabilistic nature makes them, in isolation, fundamentally unsuited for industrial product configuration, where outputs must be syntactically valid, semantically consistent with a knowledge base of hundreds…
- **Keywords:** TPU

### [R-DEIM Net: An Efficient Rationale-Augmented Dual-Expert Interaction Model for Paraphrase Detection](https://arxiv.org/abs/2609.30100v1)

- **Source:** arXiv
- **Date:** 2026-09-25
- **Summary:** Recent advances in paraphrase detection reveal a fundamental trade-off: large language models achieve high accuracy but require high computation, while efficient Siamese-BERT variants offer practical scalability with reduced transparency in rationale generation. We present R-DEIM Net, a 76M-parameter dual-expert archi…
- **Hardware relevance:** Recent advances in paraphrase detection reveal a fundamental trade-off: large language models achieve high accuracy but require high computation, while efficient Siamese-BERT variants offer practical scalability with reduced transparency in rationale generation. We present R-DEIM Net, a 76M-parameter dual-expert archi…
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
