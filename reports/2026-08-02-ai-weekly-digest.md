# Weekly AI / AI Accelerator Digest

日期：2026-08-02
範圍：過去 7 天（Asia/Taipei）

## Executive Summary

- **LLM** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **agent** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **inference** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **TPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **multimodal** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **GPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。

## 1. Top AI Papers This Week

### [Beacon: Knowing When and How to Perform Agentic Visual Reasoning](https://arxiv.org/abs/2607.28595v1)

- **Authors:** Qixun Wang, Yang Shi, Letian Cheng, Zhuoran Zhang, Yan He, Yuqi Tang, Qi Zhang, Xinlei Yu, Ruizhe Chen, Tianrun Xu, Yuanxing Zhang, Pengfei Wan, Haotian Wang, Xianghua Ying
- **Source:** arXiv
- **Date:** 2026-07-31
- **One-sentence summary:** The fundamental goal of agentic visual reasoning is to improve the success rate of multimodal large language models (MLLMs) on complex tasks, rather than merely equipping them with a sophisticated yet inefficient reasoning paradigm. In this work, we rethink agentic visual reasoning through two key dimensions of tool u…
- **Why it matters:** The fundamental goal of agentic visual reasoning is to improve the success rate of multimodal large language models (MLLMs) on complex tasks, rather than merely equipping them with a sophisticated yet inefficient reasoning paradigm. In this work, we rethink agentic visual reasoning through two key dimensions of tool u…
- **Tags:** cs.CV

### [MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers](https://arxiv.org/abs/2607.28589v1)

- **Authors:** Md. Mehrab Hossain Opi, Robiul Islam Ryad, Md. Umar Faruk
- **Source:** arXiv
- **Date:** 2026-07-31
- **One-sentence summary:** Post-training quantization (PTQ) has emerged as an effective solution for deploying Vision Transformers (ViTs) on resource-constrained devices. However, existing PTQ methods typically employ uniform bit-widths across transformer components, overlooking their heterogeneous sensitivity to quantization and leading to ine…
- **Why it matters:** Post-training quantization (PTQ) has emerged as an effective solution for deploying Vision Transformers (ViTs) on resource-constrained devices. However, existing PTQ methods typically employ uniform bit-widths across transformer components, overlooking their heterogeneous sensitivity to quantization and leading to ine…
- **Tags:** cs.CV, cs.LG

### [WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning](https://arxiv.org/abs/2607.28418v1)

- **Authors:** Haozhe Hu, Hao Wu, Peiran Yin, Chao Han, Yunpu Ma, Xiaoyu Shen
- **Source:** arXiv
- **Date:** 2026-07-31
- **One-sentence summary:** Pruning is a promising approach for improving the efficiency of LLMs. Existing static structured pruning methods are hardware-friendly and can deliver practical throughput gains, but their input-agnostic computation allocation often causes substantial accuracy degradation under aggressive sparsity.
- **Why it matters:** Pruning is a promising approach for improving the efficiency of LLMs. Existing static structured pruning methods are hardware-friendly and can deliver practical throughput gains, but their input-agnostic computation allocation often causes substantial accuracy degradation under aggressive sparsity.
- **Tags:** cs.AI, cs.CL, cs.LG

### [When Specifications Conflict: A Symmetry-Based Framework for Measuring LLM Preferences](https://arxiv.org/abs/2607.28384v1)

- **Authors:** Tairan Wang, Liang Zhou, Zikang Zhan, Pingchuan Yan
- **Source:** arXiv
- **Date:** 2026-07-30
- **One-sentence summary:** Large language models (LLMs) are increasingly required to integrate multiple sources of information that may be inconsistent or conflicting. However, there is still a lack of controllable and attributable methods for analyzing how models resolve conflicts between competing specifications.
- **Why it matters:** Large language models (LLMs) are increasingly required to integrate multiple sources of information that may be inconsistent or conflicting. However, there is still a lack of controllable and attributable methods for analyzing how models resolve conflicts between competing specifications.
- **Tags:** cs.AI

### [ObjectStream: Latent Objects as Memory Anchors for Streaming Video Understanding](https://arxiv.org/abs/2607.28312v1)

- **Authors:** Mingkang Dong, Muxin Pu, Jie Li, Bohan Guo, Songruo Chen, Bin Ren, Xu Zheng, Chen Zhao, Tianwen Qian, Mohamed Elhoseiny, Yuqian Fu
- **Source:** arXiv
- **Date:** 2026-07-30
- **One-sentence summary:** Streaming video understanding requires models to continuously retain useful visual evidence before future questions are known. Existing approaches primarily manage the growing visual context according to token importance, temporal redundancy, or segment-level relevance, but rarely organize evidence around objects that…
- **Why it matters:** Streaming video understanding requires models to continuously retain useful visual evidence before future questions are known. Existing approaches primarily manage the growing visual context according to token importance, temporal redundancy, or segment-level relevance, but rarely organize evidence around objects that…
- **Tags:** cs.CV, cs.AI

### [Capturing Token Tendencies for Training-Free Token Pruning in Multimodal Large Language Models](https://arxiv.org/abs/2607.28341v1)

- **Authors:** Jie Ma, Zhike Qiu, Jie Gao, Jiayi Ji, Qian Chen, Xiaoshuai Sun, Rongrong Ji
- **Source:** arXiv
- **Date:** 2026-07-30
- **One-sentence summary:** While visual token pruning is essential for efficient Multimodal Large Language Models (MLLMs), existing training-free methods suffer from a critical limitation: they rely on static, instantaneous heuristics to perform irreversible filtering. This approach ignores the hierarchical nature of MLLMs, where token importan…
- **Why it matters:** While visual token pruning is essential for efficient Multimodal Large Language Models (MLLMs), existing training-free methods suffer from a critical limitation: they rely on static, instantaneous heuristics to perform irreversible filtering. This approach ignores the hierarchical nature of MLLMs, where token importan…
- **Tags:** cs.CV

### [Would You Walk to the Car Wash? Revealing the Salience Bias of Large Language Models in Commonsense Reasoning](https://arxiv.org/abs/2607.28478v1)

- **Authors:** Zheng Wu, Chenhao Xue, Shijie Zheng, Yijie Lu, Cheng Yang, Zhuosheng Zhang
- **Source:** arXiv
- **Date:** 2026-07-31
- **One-sentence summary:** As large language models (LLMs) continue to advance in complex reasoning tasks, they have learned to heavily prioritize explicit conditions provided in the input. However, in everyday commonsense reasoning, this mechanism exposes a critical vulnerability which we term Salience Bias: models become easily hijacked by us…
- **Why it matters:** As large language models (LLMs) continue to advance in complex reasoning tasks, they have learned to heavily prioritize explicit conditions provided in the input. However, in everyday commonsense reasoning, this mechanism exposes a critical vulnerability which we term Salience Bias: models become easily hijacked by us…
- **Tags:** cs.CL

### [Finding Change in Satellite Archives from Text: How to Combine Before-and-After Images Efficiently](https://arxiv.org/abs/2607.28571v1)

- **Authors:** Simon Roy, Mark Bong, Giovanni Beltrame
- **Source:** arXiv
- **Date:** 2026-07-31
- **One-sentence summary:** Operational Earth observation increasingly calls for answering queries such as ``find the image pairs where a new building appeared.'' This means searching an archive of before-and-after (bi-temporal) satellite image pairs and ranking each pair by how well it matches a natural-language description of the change. The c…
- **Why it matters:** Operational Earth observation increasingly calls for answering queries such as ``find the image pairs where a new building appeared.'' This means searching an archive of before-and-after (bi-temporal) satellite image pairs and ranking each pair by how well it matches a natural-language description of the change. The c…
- **Tags:** cs.CV, cs.IR

## 2. Industry News

### [Co-Designing AI Model Attention for Fast, Interactive Long-Context Inference](https://developer.nvidia.com/blog/co-designing-ai-model-attention-for-fast-interactive-long-context-inference/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-08-01
- **Summary:** As agentic and long-context workloads become common, the context lengths increase and attention consumes a larger share of inference time (Figure 1). Because...
- **Impact:** As agentic and long-context workloads become common, the context lengths increase and attention consumes a larger share of inference time (Figure 1). Because...

### [Four Ways to Deploy More Secure AI Agents](https://developer.nvidia.com/blog/four-ways-to-deploy-more-secure-ai-agents/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-07-31
- **Summary:** Knowledge workers are increasingly integrating AI agents into their workflows. Agents that function as "digital coworkers" offer clear benefits.
- **Impact:** Knowledge workers are increasingly integrating AI agents into their workflows. Agents that function as "digital coworkers" offer clear benefits.

### [NVIDIA Video Codec SDK 13.1: Zero-Copy Transcode, AV1 B-Frames, and Frame-Accurate Seek](https://developer.nvidia.com/blog/nvidia-video-codec-sdk-13-1-zero-copy-transcode-av1-b-frames-and-frame-accurate-seek/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-07-31
- **Summary:** The demand for high-quality video continues to accelerate across industries, powering everything from immersive streaming experiences to remote collaboration,...
- **Impact:** The demand for high-quality video continues to accelerate across industries, powering everything from immersive streaming experiences to remote collaboration,...

### [Ten advances in mathematics and theoretical computer science](https://openai.com/index/ten-advances-in-mathematics)

- **Source:** OpenAI News
- **Date:** 2026-08-01
- **Summary:** OpenAI shares new results on long-standing open problems in mathematics and theoretical computer science, including advances in geometry, cryptography, and complexity.
- **Impact:** OpenAI shares new results on long-standing open problems in mathematics and theoretical computer science, including advances in geometry, cryptography, and complexity.

### [GPU Management: Why Idle GPUs Are the New Grounded Aircraft](https://huggingface.co/blog/Dharma-AI/gpu-management)

- **Source:** Hugging Face Blog
- **Date:** 2026-07-30
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [Run High-Performance Core Math at Scale with NVIDIA nvmath-python](https://developer.nvidia.com/blog/run-high-performance-core-math-at-scale-with-nvidia-nvmath-python/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-07-31
- **Summary:** NVIDIA nvmath-python is a library designed to bridge the gap between the Python scientific community and NVIDIA CUDA-X math libraries. It gives Python users...
- **Impact:** NVIDIA nvmath-python is a library designed to bridge the gap between the Python scientific community and NVIDIA CUDA-X math libraries. It gives Python users...

### [Advancing responsible AI across Europe](https://openai.com/index/advancing-responsible-ai-across-europe)

- **Source:** OpenAI News
- **Date:** 2026-07-31
- **Summary:** OpenAI shares how its safety, security, transparency, and provenance practices support responsible AI governance in Europe. The work will continue as the EU AI Act advances.
- **Impact:** OpenAI shares how its safety, security, transparency, and provenance practices support responsible AI governance in Europe. The work will continue as the EU AI Act advances.

### [Building abundant intelligence](https://openai.com/index/building-abundant-intelligence)

- **Source:** OpenAI News
- **Date:** 2026-07-31
- **Summary:** A full-stack approach to making advanced AI more capable, more affordable, and more widely useful.
- **Impact:** A full-stack approach to making advanced AI more capable, more affordable, and more widely useful.

## 3. Open Source Projects

### [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

- **Stars:** 29,315
- **Language:** Python
- **Updated date:** 2026-08-02
- **Summary:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码
- **Why it is useful:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

### [langgenius/dify](https://github.com/langgenius/dify)

- **Stars:** 151,024
- **Language:** TypeScript
- **Updated date:** 2026-08-02
- **Summary:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.
- **Why it is useful:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.

### [infiniflow/ragflow](https://github.com/infiniflow/ragflow)

- **Stars:** 86,583
- **Language:** Go
- **Updated date:** 2026-08-02
- **Summary:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs
- **Why it is useful:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

### [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

- **Stars:** 129,630
- **Language:** Python
- **Updated date:** 2026-08-02
- **Summary:** 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.
- **Why it is useful:** 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source.

### [deepset-ai/haystack](https://github.com/deepset-ai/haystack)

- **Stars:** 26,080
- **Language:** Python
- **Updated date:** 2026-08-01
- **Summary:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.
- **Why it is useful:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.

### [mem0ai/mem0](https://github.com/mem0ai/mem0)

- **Stars:** 62,287
- **Language:** Python
- **Updated date:** 2026-08-01
- **Summary:** Universal memory layer for AI Agents
- **Why it is useful:** Universal memory layer for AI Agents

### [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production)

- **Stars:** 21,223
- **Language:** Jupyter Notebook
- **Updated date:** 2026-08-01
- **Summary:** End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment.
- **Why it is useful:** End-to-end, code-first tutorials for building production-grade GenAI agents. From prototype to enterprise deployment.

### [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)

- **Stars:** 63,917
- **Language:** Python
- **Updated date:** 2026-08-01
- **Summary:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.
- **Why it is useful:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.

## 4. AI Accelerator & Hardware Trends

### [MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision Transformers](https://arxiv.org/abs/2607.28589v1)

- **Source:** arXiv
- **Date:** 2026-07-31
- **Summary:** Post-training quantization (PTQ) has emerged as an effective solution for deploying Vision Transformers (ViTs) on resource-constrained devices. However, existing PTQ methods typically employ uniform bit-widths across transformer components, overlooking their heterogeneous sensitivity to quantization and leading to ine…
- **Hardware relevance:** Post-training quantization (PTQ) has emerged as an effective solution for deploying Vision Transformers (ViTs) on resource-constrained devices. However, existing PTQ methods typically employ uniform bit-widths across transformer components, overlooking their heterogeneous sensitivity to quantization and leading to ine…
- **Keywords:** TPU

### [WIDE: Boosting Adaptive LLM Inference via Token-level Dynamic Width Pruning](https://arxiv.org/abs/2607.28418v1)

- **Source:** arXiv
- **Date:** 2026-07-31
- **Summary:** Pruning is a promising approach for improving the efficiency of LLMs. Existing static structured pruning methods are hardware-friendly and can deliver practical throughput gains, but their input-agnostic computation allocation often causes substantial accuracy degradation under aggressive sparsity.
- **Hardware relevance:** Pruning is a promising approach for improving the efficiency of LLMs. Existing static structured pruning methods are hardware-friendly and can deliver practical throughput gains, but their input-agnostic computation allocation often causes substantial accuracy degradation under aggressive sparsity.
- **Keywords:** NPU

### [When Specifications Conflict: A Symmetry-Based Framework for Measuring LLM Preferences](https://arxiv.org/abs/2607.28384v1)

- **Source:** arXiv
- **Date:** 2026-07-30
- **Summary:** Large language models (LLMs) are increasingly required to integrate multiple sources of information that may be inconsistent or conflicting. However, there is still a lack of controllable and attributable methods for analyzing how models resolve conflicts between competing specifications.
- **Hardware relevance:** Large language models (LLMs) are increasingly required to integrate multiple sources of information that may be inconsistent or conflicting. However, there is still a lack of controllable and attributable methods for analyzing how models resolve conflicts between competing specifications.
- **Keywords:** TPU, NPU

### [ObjectStream: Latent Objects as Memory Anchors for Streaming Video Understanding](https://arxiv.org/abs/2607.28312v1)

- **Source:** arXiv
- **Date:** 2026-07-30
- **Summary:** Streaming video understanding requires models to continuously retain useful visual evidence before future questions are known. Existing approaches primarily manage the growing visual context according to token importance, temporal redundancy, or segment-level relevance, but rarely organize evidence around objects that…
- **Hardware relevance:** Streaming video understanding requires models to continuously retain useful visual evidence before future questions are known. Existing approaches primarily manage the growing visual context according to token importance, temporal redundancy, or segment-level relevance, but rarely organize evidence around objects that…
- **Keywords:** GPU, ISCA

### [Capturing Token Tendencies for Training-Free Token Pruning in Multimodal Large Language Models](https://arxiv.org/abs/2607.28341v1)

- **Source:** arXiv
- **Date:** 2026-07-30
- **Summary:** While visual token pruning is essential for efficient Multimodal Large Language Models (MLLMs), existing training-free methods suffer from a critical limitation: they rely on static, instantaneous heuristics to perform irreversible filtering. This approach ignores the hierarchical nature of MLLMs, where token importan…
- **Hardware relevance:** While visual token pruning is essential for efficient Multimodal Large Language Models (MLLMs), existing training-free methods suffer from a critical limitation: they rely on static, instantaneous heuristics to perform irreversible filtering. This approach ignores the hierarchical nature of MLLMs, where token importan…
- **Keywords:** ISCA

### [Would You Walk to the Car Wash? Revealing the Salience Bias of Large Language Models in Commonsense Reasoning](https://arxiv.org/abs/2607.28478v1)

- **Source:** arXiv
- **Date:** 2026-07-31
- **Summary:** As large language models (LLMs) continue to advance in complex reasoning tasks, they have learned to heavily prioritize explicit conditions provided in the input. However, in everyday commonsense reasoning, this mechanism exposes a critical vulnerability which we term Salience Bias: models become easily hijacked by us…
- **Hardware relevance:** As large language models (LLMs) continue to advance in complex reasoning tasks, they have learned to heavily prioritize explicit conditions provided in the input. However, in everyday commonsense reasoning, this mechanism exposes a critical vulnerability which we term Salience Bias: models become easily hijacked by us…
- **Keywords:** NPU

### [Finding Change in Satellite Archives from Text: How to Combine Before-and-After Images Efficiently](https://arxiv.org/abs/2607.28571v1)

- **Source:** arXiv
- **Date:** 2026-07-31
- **Summary:** Operational Earth observation increasingly calls for answering queries such as ``find the image pairs where a new building appeared.'' This means searching an archive of before-and-after (bi-temporal) satellite image pairs and ranking each pair by how well it matches a natural-language description of the change. The c…
- **Hardware relevance:** Operational Earth observation increasingly calls for answering queries such as ``find the image pairs where a new building appeared.'' This means searching an archive of before-and-after (bi-temporal) satellite image pairs and ranking each pair by how well it matches a natural-language description of the change. The c…
- **Keywords:** ISCA

### [Fairness Pruning: Locating Demographic Bias in GLU-MLP Layers via Differential Activations](https://arxiv.org/abs/2607.28319v1)

- **Source:** arXiv
- **Date:** 2026-07-30
- **Summary:** This work presents Fairness Pruning, a lightweight structural intervention method designed for the management and future mitigation of demographic bias in large language models (LLMs). As a foundational empirical validation of this method, this work focuses on causal bias localization.
- **Hardware relevance:** This work presents Fairness Pruning, a lightweight structural intervention method designed for the management and future mitigation of demographic bias in large language models (LLMs). As a foundational empirical validation of this method, this work focuses on causal bias localization.
- **Keywords:** NPU

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
