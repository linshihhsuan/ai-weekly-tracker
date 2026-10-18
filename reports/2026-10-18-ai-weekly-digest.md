# Weekly AI / AI Accelerator Digest

日期：2026-10-18
範圍：過去 7 天（Asia/Taipei）

## Executive Summary

- **agent** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **LLM** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **TPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **GPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **inference** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **multimodal** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。

## 1. Top AI Papers This Week

### [Training-Free On-Policy Distillation](https://arxiv.org/abs/2610.22236v1)

- **Authors:** Bangji Yang, Jiajun Fan, Zhaoyu Zhu, Hongbo Ma, Ge Liu
- **Source:** arXiv
- **Date:** 2026-10-16
- **One-sentence summary:** On-policy distillation consolidates specialist models into one student at the price of rollouts, teacher passes and gradient steps for every teacher. We show that the consolidation does not need training: with forward passes only, the capabilities of separately tuned specialists can be aggregated into one model that i…
- **Why it matters:** On-policy distillation consolidates specialist models into one student at the price of rollouts, teacher passes and gradient steps for every teacher. We show that the consolidation does not need training: with forward passes only, the capabilities of separately tuned specialists can be aggregated into one model that i…
- **Tags:** cs.LG, cs.AI, cs.CL

### [DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction](https://arxiv.org/abs/2610.22130v1)

- **Authors:** Aozhong Zhang, Selcuk Gurses, Yanxia Deng, Naigang Wang, Chi-Chun Liu, Davis Wertheimer, Derrick Liu, Xin Li, Zi Yang, Felix X. -F. Ye, Penghang Yin
- **Source:** arXiv
- **Date:** 2026-10-16
- **One-sentence summary:** Key-value (KV) cache management has become a critical bottleneck for scaling Large Language Models (LLMs) to long-context scenarios due to linear memory growth. While recent eviction methods have moved beyond simple attention-score heuristics to incorporate value representations, they typically face a fundamental trad…
- **Why it matters:** Key-value (KV) cache management has become a critical bottleneck for scaling Large Language Models (LLMs) to long-context scenarios due to linear memory growth. While recent eviction methods have moved beyond simple attention-score heuristics to incorporate value representations, they typically face a fundamental trad…
- **Tags:** cs.AI

### [Grounding Generative Verification in 3D Content](https://arxiv.org/abs/2610.22360v1)

- **Authors:** Shuanglin Li, Jiaying Lin, Shuquan Ye
- **Source:** arXiv
- **Date:** 2026-10-16
- **One-sentence summary:** Recent advances in multimodal large language models (MLLMs) and 3D generation have expanded 3D understanding and synthesis. However, beyond visual fidelity, task-specific correctness grounded in 3D evidence remains a major challenge.
- **Why it matters:** Recent advances in multimodal large language models (MLLMs) and 3D generation have expanded 3D understanding and synthesis. However, beyond visual fidelity, task-specific correctness grounded in 3D evidence remains a major challenge.
- **Tags:** cs.CV

### [FALCON: FPGA-Accelerated Latency-Certifiable Occupancy Networks for Camera-Based Autonomous Driving](https://arxiv.org/abs/2610.22143v1)

- **Authors:** Haohua Que, Mingkai Liu, Handong Yao
- **Source:** arXiv
- **Date:** 2026-10-16
- **One-sentence summary:** A perception system that must brake for a pedestrian does not need a low average latency. It must deliver an answer before the deadline on every frame, the worst case included.
- **Why it matters:** A perception system that must brake for a pedestrian does not need a low average latency. It must deliver an answer before the deadline on every frame, the worst case included.
- **Tags:** cs.CV

### [BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks](https://arxiv.org/abs/2610.22256v1)

- **Authors:** Max Zhu, Bohang Sun, Pietro Lio, Jialin Yu
- **Source:** arXiv
- **Date:** 2026-10-16
- **One-sentence summary:** Reducing memory use in large language model (LLM) training is an ongoing challenge. Activation checkpointing saves memory by recomputation, while lossy compression changes the stored activations.
- **Why it matters:** Reducing memory use in large language model (LLM) training is an ongoing challenge. Activation checkpointing saves memory by recomputation, while lossy compression changes the stored activations.
- **Tags:** cs.LG

### [Architecting for Hardware Diversity: Meta's End-to-End Co-Design for High-Performance AI Training on AMD GPUs](https://arxiv.org/abs/2610.22230v1)

- **Authors:** Haoyu Zhang, Arshad Rahman, Adnan Aziz, Ajith Prabhudev, Amin Farmahini, Ben Rhoads, Benson Ma, Brian Shi, Cen Zhao, CK Luk, Dingming Wu, Emad El-Haraty, Eric Chen, Frank Li, Gary Huang, Gefei Zuo, Haoran Zhang, Hiwot Kassa, Hongyi Zeng, Jack Taylor, Jeremy Hadidjojo, John Donati, Jonathan Sheffield, Julio Machado Silva, Karthik Ganesan, Kent Russell, KR Kishore, Lei Tian, Liu Ke, Muhammad Osama, Peng Chen, Rakesh Hemnani, Ryan Swann, Saleel Kudchadker, Shankar Yanamandram, Shobhit Kanaujia, Shucai Xiao, Srinath Bayareddy, Srinivas Vaidyanathan, Sudharssun Subramanian, Supadchaya Puangpontip, Taylor Robie, Tianhao Huang, Tyler Hart, Viswesh Sankaran, Weijun Jiang, Wenkai Du, Xiaodong Wang, Xiaohu Guo, Yao Rong, Yinbin Ma, Yue Dong, Yuzhen Huang, Yvonne Liu, Zhan Shu, Dan Rabinovitsj, Ajit Mathews, Chunqiang Tang
- **Source:** arXiv
- **Date:** 2026-10-16
- **One-sentence summary:** Meta deploys a heterogeneous fleet comprising NVIDIA GPUs, AMD GPUs, and proprietary MTIA accelerators to reduce costs and mitigate vendor lock-in. However, the extensive history of NVIDIA-specific optimizations hinders performance portability to other hardware.
- **Why it matters:** Meta deploys a heterogeneous fleet comprising NVIDIA GPUs, AMD GPUs, and proprietary MTIA accelerators to reduce costs and mitigate vendor lock-in. However, the extensive history of NVIDIA-specific optimizations hinders performance portability to other hardware.
- **Tags:** cs.DC, cs.AR, cs.LG

### [Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries](https://arxiv.org/abs/2610.22273v1)

- **Authors:** Anikait Singh, Teresa Zhang, Yoonho Lee, Roshen Sanjay Nair, Aviral Kumar, Chelsea Finn
- **Source:** arXiv
- **Date:** 2026-10-16
- **One-sentence summary:** Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid h…
- **Why it matters:** Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid h…
- **Tags:** cs.LG, cs.AI, cs.CL

### [MJev-Spatial: System One Spatial Intelligence via Native Attention Matching](https://arxiv.org/abs/2610.22276v1)

- **Authors:** Luozheng Qin, Yuhan Zhu, Changhai Zhou, Qian Qiao, Jun Gao, Yuhua Zhou, Harry Zhang, Xiangyu Zeng, Yuxuan Liu, Kaijie Chen, Andrew Chen, Pony Ma
- **Source:** arXiv
- **Date:** 2026-10-16
- **One-sentence summary:** Spatial intelligence lets an agent perceive and act in the physical world, and many of its judgments must be made at interaction rates: which spatial relation holds, how far an object is, or where to place it. Vision-language models (VLMs) produce these answers by free-form text generation, paying for autoregressive d…
- **Why it matters:** Spatial intelligence lets an agent perceive and act in the physical world, and many of its judgments must be made at interaction rates: which spatial relation holds, how far an object is, or where to place it. Vision-language models (VLMs) produce these answers by free-form text generation, paying for autoregressive d…
- **Tags:** cs.CV

## 2. Industry News

### [Code, Test, and Deploy on One Machine with NVIDIA RTX Spark](https://developer.nvidia.com/blog/code-test-and-deploy-on-one-machine-with-nvidia-rtx-spark/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-10-17
- **Summary:** AI agents are changing how software gets built. Developers have gone from writing every line of code by hand to directing agents that write most of the code.
- **Impact:** AI agents are changing how software gets built. Developers have gone from writing every line of code by hand to directing agents that write most of the code.

### [Optimizing Agent Reliability and Tool Calling Efficiency for Chip Design Using NVIDIA NeMo Gym](https://developer.nvidia.com/blog/optimizing-agent-reliability-and-tool-calling-efficiency-for-chip-design-using-nvidia-nemo-gym/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-10-15
- **Summary:** AI agents offer remarkable productivity gains in complex chip design workflows, but their tendency to generate plausible yet incorrect artifacts makes...
- **Impact:** AI agents offer remarkable productivity gains in complex chip design workflows, but their tendency to generate plausible yet incorrect artifacts makes...

### [How Itaú is building generative AI for its entire customer base](https://openai.com/index/itau-generative-ai)

- **Source:** OpenAI News
- **Date:** 2026-10-17
- **Summary:** With ia.i, a conversational interface, and the IARA governance platform, Itaú is applying its AI First strategy to customers and employees — in one of Brazil’s most regulated sectors.
- **Impact:** With ia.i, a conversational interface, and the IARA governance platform, Itaú is applying its AI First strategy to customers and employees — in one of Brazil’s most regulated sectors.

### [Amp puts AI agents to work beyond code with OpenAI models](https://openai.com/index/amp-beyond-coding)

- **Source:** OpenAI News
- **Date:** 2026-10-14
- **Summary:** See how Amp pushes the frontier of what agents can do with GPT-6 Astra, Ultrafast, GPT-Live-1, and Sign in with ChatGPT.
- **Impact:** See how Amp pushes the frontier of what agents can do with GPT-6 Astra, Ultrafast, GPT-Live-1, and Sign in with ChatGPT.

### [How to Rewrite Apache Spark UDFs for GPU Acceleration with AI Agents](https://developer.nvidia.com/blog/rewrite-apache-spark-udfs-gpu-acceleration-ai-agents/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-10-14
- **Summary:** Enterprise applications have become increasingly demanding. Agentic AI has compounded the need for vast amounts of enterprise data with frequent, complex...
- **Impact:** Enterprise applications have become increasingly demanding. Agentic AI has compounded the need for vast amounts of enterprise data with frequent, complex...

### [Benefit Street Partners answers questions faster with Codex](https://openai.com/index/benefit-street-partners)

- **Source:** OpenAI News
- **Date:** 2026-10-16
- **Summary:** Anant Kumar builds tools to compare loan valuations and analyze credit agreements, using Codex for code review and faster follow-ups.
- **Impact:** Anant Kumar builds tools to compare loan valuations and analyze credit agreements, using Codex for code review and faster follow-ups.

### [Stack Overflow for Agents triples signups with ChatGPT plugin](https://openai.com/index/stack-overflow-chatgpt-plugin)

- **Source:** OpenAI News
- **Date:** 2026-10-16
- **Summary:** Two engineers shipped Stack Overflow for Agents in a few weeks with Codex, and its ChatGPT plugin helped drive up to 10× growth in agent creation.
- **Impact:** Two engineers shipped Stack Overflow for Agents in a few weeks with Codex, and its ChatGPT plugin helped drive up to 10× growth in agent creation.

### [NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-10-16
- **Summary:** Always-on agents are taking on longer, more complex enterprise workflows. A single request can involve reading a document, checking information across sources,...
- **Impact:** Always-on agents are taking on longer, more complex enterprise workflows. A single request can involve reading a document, checking information across sources,...

## 3. Open Source Projects

### [langgenius/dify](https://github.com/langgenius/dify)

- **Stars:** 158,742
- **Language:** Python
- **Updated date:** 2026-10-18
- **Summary:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.
- **Why it is useful:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.

### [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production)

- **Stars:** 21,724
- **Language:** Jupyter Notebook
- **Updated date:** 2026-10-17
- **Summary:** End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment.
- **Why it is useful:** End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment.

### [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)

- **Stars:** 75,609
- **Language:** Python
- **Updated date:** 2026-10-18
- **Summary:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.
- **Why it is useful:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.

### [deepset-ai/haystack](https://github.com/deepset-ai/haystack)

- **Stars:** 26,762
- **Language:** Python
- **Updated date:** 2026-10-17
- **Summary:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.
- **Why it is useful:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.

### [mem0ai/mem0](https://github.com/mem0ai/mem0)

- **Stars:** 67,369
- **Language:** Python
- **Updated date:** 2026-10-18
- **Summary:** The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists.
- **Why it is useful:** The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists.

### [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)

- **Stars:** 67,260
- **Language:** JavaScript
- **Updated date:** 2026-10-17
- **Summary:** Stop renting your intelligence. Own it with AnythingLLM.
- **Why it is useful:** Stop renting your intelligence. Own it with AnythingLLM.

### [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

- **Stars:** 142,152
- **Language:** Python
- **Updated date:** 2026-10-18
- **Summary:** 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- **Why it is useful:** 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.

### [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents)

- **Stars:** 24,615
- **Language:** Jupyter Notebook
- **Updated date:** 2026-10-17
- **Summary:** 50+ tutorials and implementations for Generative AI Agent techniques, from basic conversational bots to complex multi-agent systems.
- **Why it is useful:** 50+ tutorials and implementations for Generative AI Agent techniques, from basic conversational bots to complex multi-agent systems.

## 4. AI Accelerator & Hardware Trends

### [Training-Free On-Policy Distillation](https://arxiv.org/abs/2610.22236v1)

- **Source:** arXiv
- **Date:** 2026-10-16
- **Summary:** On-policy distillation consolidates specialist models into one student at the price of rollouts, teacher passes and gradient steps for every teacher. We show that the consolidation does not need training: with forward passes only, the capabilities of separately tuned specialists can be aggregated into one model that i…
- **Hardware relevance:** On-policy distillation consolidates specialist models into one student at the price of rollouts, teacher passes and gradient steps for every teacher. We show that the consolidation does not need training: with forward passes only, the capabilities of separately tuned specialists can be aggregated into one model that i…
- **Keywords:** TPU, GPU, NPU

### [DropKV: Decoupling Residual-Output Perturbation for Near-Optimal KV-Cache Eviction](https://arxiv.org/abs/2610.22130v1)

- **Source:** arXiv
- **Date:** 2026-10-16
- **Summary:** Key-value (KV) cache management has become a critical bottleneck for scaling Large Language Models (LLMs) to long-context scenarios due to linear memory growth. While recent eviction methods have moved beyond simple attention-score heuristics to incorporate value representations, they typically face a fundamental trad…
- **Hardware relevance:** Key-value (KV) cache management has become a critical bottleneck for scaling Large Language Models (LLMs) to long-context scenarios due to linear memory growth. While recent eviction methods have moved beyond simple attention-score heuristics to incorporate value representations, they typically face a fundamental trad…
- **Keywords:** TPU

### [Grounding Generative Verification in 3D Content](https://arxiv.org/abs/2610.22360v1)

- **Source:** arXiv
- **Date:** 2026-10-16
- **Summary:** Recent advances in multimodal large language models (MLLMs) and 3D generation have expanded 3D understanding and synthesis. However, beyond visual fidelity, task-specific correctness grounded in 3D evidence remains a major challenge.
- **Hardware relevance:** Recent advances in multimodal large language models (MLLMs) and 3D generation have expanded 3D understanding and synthesis. However, beyond visual fidelity, task-specific correctness grounded in 3D evidence remains a major challenge.
- **Keywords:** TPU, NPU

### [FALCON: FPGA-Accelerated Latency-Certifiable Occupancy Networks for Camera-Based Autonomous Driving](https://arxiv.org/abs/2610.22143v1)

- **Source:** arXiv
- **Date:** 2026-10-16
- **Summary:** A perception system that must brake for a pedestrian does not need a low average latency. It must deliver an answer before the deadline on every frame, the worst case included.
- **Hardware relevance:** A perception system that must brake for a pedestrian does not need a low average latency. It must deliver an answer before the deadline on every frame, the worst case included.
- **Keywords:** TPU, GPU

### [BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks](https://arxiv.org/abs/2610.22256v1)

- **Source:** arXiv
- **Date:** 2026-10-16
- **Summary:** Reducing memory use in large language model (LLM) training is an ongoing challenge. Activation checkpointing saves memory by recomputation, while lossy compression changes the stored activations.
- **Hardware relevance:** Reducing memory use in large language model (LLM) training is an ongoing challenge. Activation checkpointing saves memory by recomputation, while lossy compression changes the stored activations.
- **Keywords:** GPU

### [Architecting for Hardware Diversity: Meta's End-to-End Co-Design for High-Performance AI Training on AMD GPUs](https://arxiv.org/abs/2610.22230v1)

- **Source:** arXiv
- **Date:** 2026-10-16
- **Summary:** Meta deploys a heterogeneous fleet comprising NVIDIA GPUs, AMD GPUs, and proprietary MTIA accelerators to reduce costs and mitigate vendor lock-in. However, the extensive history of NVIDIA-specific optimizations hinders performance portability to other hardware.
- **Hardware relevance:** Meta deploys a heterogeneous fleet comprising NVIDIA GPUs, AMD GPUs, and proprietary MTIA accelerators to reduce costs and mitigate vendor lock-in. However, the extensive history of NVIDIA-specific optimizations hinders performance portability to other hardware.
- **Keywords:** GPU, HBM

### [MJev-Spatial: System One Spatial Intelligence via Native Attention Matching](https://arxiv.org/abs/2610.22276v1)

- **Source:** arXiv
- **Date:** 2026-10-16
- **Summary:** Spatial intelligence lets an agent perceive and act in the physical world, and many of its judgments must be made at interaction rates: which spatial relation holds, how far an object is, or where to place it. Vision-language models (VLMs) produce these answers by free-form text generation, paying for autoregressive d…
- **Hardware relevance:** Spatial intelligence lets an agent perceive and act in the physical world, and many of its judgments must be made at interaction rates: which spatial relation holds, how far an object is, or where to place it. Vision-language models (VLMs) produce these answers by free-form text generation, paying for autoregressive d…
- **Keywords:** TPU, GPU

### [Training Reasoning Models to Generate Diverse Scientific Ideas](https://arxiv.org/abs/2610.22324v1)

- **Source:** arXiv
- **Date:** 2026-10-16
- **Summary:** One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity.
- **Hardware relevance:** One of the first steps of a research pipeline is generating ideas. Large Language Models (LLMs) are increasingly used to automate this step, but most of this work optimizes the quality of individual ideas, while overlooking diversity.
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
