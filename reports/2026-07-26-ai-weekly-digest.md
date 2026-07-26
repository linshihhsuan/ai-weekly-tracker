# Weekly AI / AI Accelerator Digest

日期：2026-07-26
範圍：過去 7 天（Asia/Taipei）

## Executive Summary

- **agent** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **TPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **LLM** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **inference** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **GPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **quantization** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。

## 1. Top AI Papers This Week

### [Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks](https://arxiv.org/abs/2607.21482v1)

- **Authors:** Mack Nixon, Liam Wright, Yevgeniya Kovalchuk, Alison Fang-Wei Wu, Martin Danka, Andy Boyd, David Bann
- **Source:** arXiv
- **Date:** 2026-07-24
- **One-sentence summary:** Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models. Their adoption in research using personal data is constrained by governance requirements that typically prohibit data transmission to external services.
- **Why it matters:** Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models. Their adoption in research using personal data is constrained by governance requirements that typically prohibit data transmission to external services.
- **Tags:** cs.AI, cs.CL

### [Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs](https://arxiv.org/abs/2607.21291v1)

- **Authors:** Yidu Wu, Xiang Wang, Kejie Zhao, Zhangchi Wang, Qinghai Guo, Xiaoying Tang
- **Source:** arXiv
- **Date:** 2026-07-23
- **One-sentence summary:** Large language models (LLMs) achieve strong generation and reasoning performance, but the Transformer architecture incurs high inference cost. Existing acceleration methods often rely on task-specific fine-tuning or training from scratch, increasing adaptation cost and limiting cross-task usability.
- **Why it matters:** Large language models (LLMs) achieve strong generation and reasoning performance, but the Transformer architecture incurs high inference cost. Existing acceleration methods often rely on task-specific fine-tuning or training from scratch, increasing adaptation cost and limiting cross-task usability.
- **Tags:** cs.CL, cs.LG

### [Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning via Prolog](https://arxiv.org/abs/2607.21412v1)

- **Authors:** Bartolomeo Bogliolo
- **Source:** arXiv
- **Date:** 2026-07-23
- **One-sentence summary:** Large Language Models (LLMs) excel at natural language understanding and generation but remain unreliable for multi-step logical reasoning, especially in safety-critical or compliance-sensitive domains. Recent neuro-symbolic approaches address this gap by coupling neural models with external symbolic engines, yet most…
- **Why it matters:** Large Language Models (LLMs) excel at natural language understanding and generation but remain unreliable for multi-step logical reasoning, especially in safety-critical or compliance-sensitive domains. Recent neuro-symbolic approaches address this gap by coupling neural models with external symbolic engines, yet most…
- **Tags:** cs.AI, cs.CL, cs.SE

### [Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context](https://arxiv.org/abs/2607.21535v1)

- **Authors:** Alagappan Valliappan
- **Source:** arXiv
- **Date:** 2026-07-24
- **One-sentence summary:** Speculative decoding accelerates autoregressive generation by having a cheap draft propose tokens that a target verifies in parallel. Frontier models increasingly ship a built-in Multi-Token-Prediction (MTP/NEXTN) draft head under the assumption that the draft is negligibly cheap.
- **Why it matters:** Speculative decoding accelerates autoregressive generation by having a cheap draft propose tokens that a target verifies in parallel. Frontier models increasingly ship a built-in Multi-Token-Prediction (MTP/NEXTN) draft head under the assumption that the draft is negligibly cheap.
- **Tags:** cs.LG, cs.CL, cs.PF

### [KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training Quantization of Diffusion Transformers](https://arxiv.org/abs/2607.21446v1)

- **Authors:** Yann Bouquet, Alireza Khodamoradi, Kristof Denolf, Mathieu Salzmann
- **Source:** arXiv
- **Date:** 2026-07-23
- **One-sentence summary:** Post-training quantization (PTQ) of diffusion transformers (DiTs) to W4A4 severely degrades output quality, because activations entering each linear layer contain outliers that 4-bit formats cannot represent. The standard fix applies an invertible linear transform to the activations and its inverse to the weights befo…
- **Why it matters:** Post-training quantization (PTQ) of diffusion transformers (DiTs) to W4A4 severely degrades output quality, because activations entering each linear layer contain outliers that 4-bit formats cannot represent. The standard fix applies an invertible linear transform to the activations and its inverse to the weights befo…
- **Tags:** cs.LG, cs.CV

### [Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems](https://arxiv.org/abs/2607.21503v1)

- **Authors:** Gaurav Dadhich
- **Source:** arXiv
- **Date:** 2026-07-24
- **One-sentence summary:** Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token…
- **Why it matters:** Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token…
- **Tags:** cs.AI, cs.IR

### [OpenForgeRL: Train Harness-native Agents in Any Environment](https://arxiv.org/abs/2607.21557v1)

- **Authors:** Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao
- **Source:** arXiv
- **Date:** 2026-07-24
- **One-sentence summary:** Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex harnesses also make agents hard to train end-to-end with open infrastructure, whose SFT/RL stacks cannot natively expres…
- **Why it matters:** Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex harnesses also make agents hard to train end-to-end with open infrastructure, whose SFT/RL stacks cannot natively expres…
- **Tags:** cs.AI, cs.CL

### [Capital Markets LLM Reliability Score (CM-LRS): From Plausible to Bankable](https://arxiv.org/abs/2607.21340v1)

- **Authors:** Prerit Ahuja
- **Source:** arXiv
- **Date:** 2026-07-23
- **One-sentence summary:** In capital-markets workflows the question is rarely whether a large language model can produce a fluent draft, but whether the draft is bankable: defensible in front of a counter-party or a regulator, with the documents in hand. Existing methods address parts of that gap: open-domain QA benchmarks reward surface accur…
- **Why it matters:** In capital-markets workflows the question is rarely whether a large language model can produce a fluent draft, but whether the draft is bankable: defensible in front of a counter-party or a regulator, with the documents in hand. Existing methods address parts of that gap: open-domain QA benchmarks reward surface accur…
- **Tags:** cs.CL

## 2. Industry News

### [Debugging Ray Tracing Applications Using NVIDIA OptiX Toolkit](https://developer.nvidia.com/blog/debugging-ray-tracing-applications-using-nvidia-optix-toolkit/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-07-24
- **Summary:** NVIDIA OptiX ray tracing engine is an application framework for achieving optimal ray tracing performance on the GPU. Applications using OptiX can fail in ways...
- **Impact:** NVIDIA OptiX ray tracing engine is an application framework for achieving optimal ray tracing performance on the GPU. Applications using OptiX can fail in ways...

### [ModelExpress: Distributing Model Artifacts at the Speed of Light](https://developer.nvidia.com/blog/modelexpress-distributing-model-artifacts-at-the-speed-of-light/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-07-25
- **Summary:** Every byte moved has a cost. As model checkpoints grow to hundreds of gigabytes or even a terabyte, that cost adds up quickly.
- **Impact:** Every byte moved has a cost. As model checkpoints grow to hundreds of gigabytes or even a terabyte, that cost adds up quickly.

### [NVIDIA Vera CPU: Olympus Cores Built for Maximum Single-Thread Performance in Agentic AI](https://developer.nvidia.com/blog/inside-nvidia-vera-cpu-olympus-cores-built-for-maximum-single-threaded-performance-in-agentic-ai/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-07-22
- **Summary:** Agentic AI shifts more of the critical execution path onto the CPU. Agents operate in sandboxes to execute code, invoke tools, retrieve context, interact with...
- **Impact:** Agentic AI shifts more of the critical execution path onto the CPU. Agents operate in sandboxes to execute code, invoke tools, retrieve context, interact with...

### [Make Long-Running NVIDIA TensorRT Engine Builds Observable and Cancelable in Python or C++](https://developer.nvidia.com/blog/make-long-running-nvidia-tensorrt-engine-builds-observable-and-cancelable-in-python-or-c/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-07-23
- **Summary:** A TensorRT engine build can take seconds to many minutes. Large strongly typed models, deep tactic search, and a cold timing cache on a brand-new GPU SKU can...
- **Impact:** A TensorRT engine build can take seconds to many minutes. Large strongly typed models, deep tactic search, and a cold timing cache on a brand-new GPU SKU can...

### [Introducing OpenAI Presence](https://openai.com/index/introducing-openai-presence)

- **Source:** OpenAI News
- **Date:** 2026-07-22
- **Summary:** Introducing OpenAI Presence, a proven enterprise AI agent platform that helps organizations deploy trusted voice and chat agents for customer and internal workflows.
- **Impact:** Introducing OpenAI Presence, a proven enterprise AI agent platform that helps organizations deploy trusted voice and chat agents for customer and internal workflows.

### [Bringing Nunchaku 4-bit Diffusion Inference to Diffusers](https://huggingface.co/blog/nunchaku-diffusers)

- **Source:** Hugging Face Blog
- **Date:** 2026-07-23
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [Start Customizing NVIDIA Nemotron 3 Nano with Prime Intellect Lab in Minutes](https://developer.nvidia.com/blog/start-customizing-nvidia-nemotron-3-nano-with-prime-intellect-lab-in-minutes/)

- **Source:** NVIDIA Technical Blog
- **Date:** 2026-07-24
- **Summary:** Customization is what enables developers to take a general model and tailor it to use cases, domains, languages, and more. However, customization comes with a...
- **Impact:** Customization is what enables developers to take a general model and tailor it to use cases, domains, languages, and more. However, customization comes with a...

### [Building AI infrastructure with the Effingham County community](https://openai.com/index/building-ai-infrastructure-with-the-effingham-county-community)

- **Source:** OpenAI News
- **Date:** 2026-07-22
- **Summary:** OpenAI announces Project Camellia in Effingham County, Georgia, with commitments to responsible energy, community investment, jobs, and access to Codex.
- **Impact:** OpenAI announces Project Camellia in Effingham County, Georgia, with commitments to responsible energy, community investment, jobs, and access to Codex.

## 3. Open Source Projects

### [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

- **Stars:** 19,895
- **Language:** Python
- **Updated date:** 2026-07-26
- **Summary:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码
- **Why it is useful:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

### [langgenius/dify](https://github.com/langgenius/dify)

- **Stars:** 150,258
- **Language:** TypeScript
- **Updated date:** 2026-07-26
- **Summary:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.
- **Why it is useful:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.

### [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)

- **Stars:** 62,435
- **Language:** Python
- **Updated date:** 2026-07-26
- **Summary:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.
- **Why it is useful:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.

### [cactus-compute/cactus](https://github.com/cactus-compute/cactus)

- **Stars:** 5,538
- **Language:** C++
- **Updated date:** 2026-07-26
- **Summary:** Quantization, kernels, runtime and inference engine for mobiles, wearables, smart home and robots.
- **Why it is useful:** Quantization, kernels, runtime and inference engine for mobiles, wearables, smart home and robots.

### [deepset-ai/haystack](https://github.com/deepset-ai/haystack)

- **Stars:** 26,015
- **Language:** Python
- **Updated date:** 2026-07-25
- **Summary:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.
- **Why it is useful:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.

### [arc53/DocsGPT](https://github.com/arc53/DocsGPT)

- **Stars:** 18,046
- **Language:** Python
- **Updated date:** 2026-07-26
- **Summary:** Private AI platform for agents, assistants and enterprise search. Built-in Agent Builder, Deep research, Document analysis, Multi-model support, and API connectivity for agents.
- **Why it is useful:** Private AI platform for agents, assistants and enterprise search. Built-in Agent Builder, Deep research, Document analysis, Multi-model support, and API connectivity for agents.

### [infiniflow/ragflow](https://github.com/infiniflow/ragflow)

- **Stars:** 85,999
- **Language:** Go
- **Updated date:** 2026-07-25
- **Summary:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs
- **Why it is useful:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

### [mem0ai/mem0](https://github.com/mem0ai/mem0)

- **Stars:** 61,688
- **Language:** TypeScript
- **Updated date:** 2026-07-25
- **Summary:** Universal memory layer for AI Agents
- **Why it is useful:** Universal memory layer for AI Agents

## 4. AI Accelerator & Hardware Trends

### [Agentic coding without the cloud: evaluating open-weight large language models on longitudinal data preparation tasks](https://arxiv.org/abs/2607.21482v1)

- **Source:** arXiv
- **Date:** 2026-07-24
- **Summary:** Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models. Their adoption in research using personal data is constrained by governance requirements that typically prohibit data transmission to external services.
- **Hardware relevance:** Large language models (LLMs) and agents are now widely used tools in code development, with data typically sent to third-party cloud-based models. Their adoption in research using personal data is constrained by governance requirements that typically prohibit data transmission to external services.
- **Keywords:** TPU

### [Adaptive Depth Sparse Framework: Similarity-Driven Resource Allocation for Pre-Trained LLMs](https://arxiv.org/abs/2607.21291v1)

- **Source:** arXiv
- **Date:** 2026-07-23
- **Summary:** Large language models (LLMs) achieve strong generation and reasoning performance, but the Transformer architecture incurs high inference cost. Existing acceleration methods often rely on task-specific fine-tuning or training from scratch, increasing adaptation cost and limiting cross-task usability.
- **Hardware relevance:** Large language models (LLMs) achieve strong generation and reasoning performance, but the Transformer architecture incurs high inference cost. Existing acceleration methods often rely on task-specific fine-tuning or training from scratch, increasing adaptation cost and limiting cross-task usability.
- **Keywords:** TPU, NPU

### [Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning via Prolog](https://arxiv.org/abs/2607.21412v1)

- **Source:** arXiv
- **Date:** 2026-07-23
- **Summary:** Large Language Models (LLMs) excel at natural language understanding and generation but remain unreliable for multi-step logical reasoning, especially in safety-critical or compliance-sensitive domains. Recent neuro-symbolic approaches address this gap by coupling neural models with external symbolic engines, yet most…
- **Hardware relevance:** Large Language Models (LLMs) excel at natural language understanding and generation but remain unreliable for multi-step logical reasoning, especially in safety-critical or compliance-sensitive domains. Recent neuro-symbolic approaches address this gap by coupling neural models with external symbolic engines, yet most…
- **Keywords:** TPU

### [Windowed-MTP: Removing the Full-Context Draft-KV Tax at Million-Token Context](https://arxiv.org/abs/2607.21535v1)

- **Source:** arXiv
- **Date:** 2026-07-24
- **Summary:** Speculative decoding accelerates autoregressive generation by having a cheap draft propose tokens that a target verifies in parallel. Frontier models increasingly ship a built-in Multi-Token-Prediction (MTP/NEXTN) draft head under the assumption that the draft is negligibly cheap.
- **Hardware relevance:** Speculative decoding accelerates autoregressive generation by having a cheap draft propose tokens that a target verifies in parallel. Frontier models increasingly ship a built-in Multi-Token-Prediction (MTP/NEXTN) draft head under the assumption that the draft is negligibly cheap.
- **Keywords:** TPU, GPU, NPU

### [KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training Quantization of Diffusion Transformers](https://arxiv.org/abs/2607.21446v1)

- **Source:** arXiv
- **Date:** 2026-07-23
- **Summary:** Post-training quantization (PTQ) of diffusion transformers (DiTs) to W4A4 severely degrades output quality, because activations entering each linear layer contain outliers that 4-bit formats cannot represent. The standard fix applies an invertible linear transform to the activations and its inverse to the weights befo…
- **Hardware relevance:** Post-training quantization (PTQ) of diffusion transformers (DiTs) to W4A4 severely degrades output quality, because activations entering each linear layer contain outliers that 4-bit formats cannot represent. The standard fix applies an invertible linear transform to the activations and its inverse to the weights befo…
- **Keywords:** TPU, GPU

### [Agentic Context Management: Solving Agent Memory and Cost by Treating Them as Lifecycle and Architecture Problems](https://arxiv.org/abs/2607.21503v1)

- **Source:** arXiv
- **Date:** 2026-07-24
- **Summary:** Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token…
- **Hardware relevance:** Production AI agents' failures are less often due to an inability to reason well and more often because they cannot manage what is in their reasoning context: conversation histories, large prompts, large tool definitions, and ballooning tool outputs. Agents drown in their own accumulating history while paying a token…
- **Keywords:** TPU

### [Capital Markets LLM Reliability Score (CM-LRS): From Plausible to Bankable](https://arxiv.org/abs/2607.21340v1)

- **Source:** arXiv
- **Date:** 2026-07-23
- **Summary:** In capital-markets workflows the question is rarely whether a large language model can produce a fluent draft, but whether the draft is bankable: defensible in front of a counter-party or a regulator, with the documents in hand. Existing methods address parts of that gap: open-domain QA benchmarks reward surface accur…
- **Hardware relevance:** In capital-markets workflows the question is rarely whether a large language model can produce a fluent draft, but whether the draft is bankable: defensible in front of a counter-party or a regulator, with the documents in hand. Existing methods address parts of that gap: open-domain QA benchmarks reward surface accur…
- **Keywords:** TPU

### [SPORD: A Simulation-Propose-then-OR-Dispose Approach for Supply Chain Planning](https://arxiv.org/abs/2607.21354v1)

- **Source:** arXiv
- **Date:** 2026-07-23
- **Summary:** For years, supply chain planning at e-commerce firms has operated as a collection of isolated projects. Each planning task from static network planning to dynamic warehouse assortment planning requires analysts to spend weeks building models from scratch, calibrating and persuading executives to act on outputs they ca…
- **Hardware relevance:** For years, supply chain planning at e-commerce firms has operated as a collection of isolated projects. Each planning task from static network planning to dynamic warehouse assortment planning requires analysts to spend weeks building models from scratch, calibrating and persuading executives to act on outputs they ca…
- **Keywords:** TPU, GPU

## 5. What I Should Study Next

- agent
- TPU
- FPGA / ASIC accelerator architecture
- systolic arrays and dataflow
- quantized inference optimization

## 6. Suggested Reading Order

1. 先讀 Industry News，建立本週產業背景。
2. 接著瀏覽 Open Source Projects，動手理解工具與工作流。
3. 再讀 Top AI Papers，掌握方法、實驗與 benchmark。
4. 最後深入 AI Accelerator & Hardware Trends，串連架構、效能與系統限制。
