# Weekly AI / AI Accelerator Digest

日期：2026-08-09
範圍：過去 7 天（Asia/Taipei）

## Executive Summary

- **inference** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **LLM** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **multimodal** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **agent** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **TPU** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。
- **quantization** 是本週高頻主題，相關內容橫跨研究、產業或硬體動態。

## 1. Top AI Papers This Week

### [PaDoc: Layout-Grounded Parallel Decoding for Document Parsing](https://arxiv.org/abs/2608.06146v1)

- **Authors:** Hao Yu, Jiabo Zhan, Kang Liu, Linnan Zhao, Dongxu Yue, Rui Chen, Jinglin Wang, Chong Sun, Chen Li, Jing Lyu, Chun Yuan
- **Source:** arXiv
- **Date:** 2026-08-06
- **One-sentence summary:** End-to-end document parsers provide a unified interface, but serialize page layouts and regional contents into one autoregressive sequence. This formulation forces independent regions onto a decoding path whose length grows with the total content, whereas crop-based two-stage parsers expose region-level parallelism at…
- **Why it matters:** End-to-end document parsers provide a unified interface, but serialize page layouts and regional contents into one autoregressive sequence. This formulation forces independent regions onto a decoding path whose length grows with the total content, whereas crop-based two-stage parsers expose region-level parallelism at…
- **Tags:** cs.AI

### [TS-RAG: Retrieval Augmented Generation for Time Series Forecasting](https://arxiv.org/abs/2608.06223v1)

- **Authors:** Yixiong Xiao, Congxi Xiao, Jingbo Zhou
- **Source:** arXiv
- **Date:** 2026-08-07
- **One-sentence summary:** While deep learning models, particularly transformer-based architectures, have shown impressive performance in time series forecasting, the application of retrieval-augmented generation (RAG) in this domain remains limited. Since RAG has proven effective in enhancing the capabilities of large language models by incorp…
- **Why it matters:** While deep learning models, particularly transformer-based architectures, have shown impressive performance in time series forecasting, the application of retrieval-augmented generation (RAG) in this domain remains limited. Since RAG has proven effective in enhancing the capabilities of large language models by incorp…
- **Tags:** cs.AI, cs.LG

### [NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering](https://arxiv.org/abs/2608.06292v1)

- **Authors:** Jonas Gann, Michael Gertz
- **Source:** arXiv
- **Date:** 2026-08-07
- **One-sentence summary:** Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely opaque: intermediate reasoning steps are difficult to verify and cannot be reliably attributed to specific evidence.
- **Why it matters:** Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely opaque: intermediate reasoning steps are difficult to verify and cannot be reliably attributed to specific evidence.
- **Tags:** cs.CL, cs.SC

### [Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers](https://arxiv.org/abs/2608.06111v1)

- **Authors:** Haris Riaz, Hyungji Kim, Mihai Surdeanu
- **Source:** arXiv
- **Date:** 2026-08-06
- **One-sentence summary:** Positional embeddings (PE) in Transformers encode token distance and order but are largely agnostic to \textit{syntactic structure}. We introduce \textbf{S}yntax-\textbf{i}nformed \textbf{P}ositional \textbf{E}mbeddings (\textbf{SiPE}), which learns a lightweight syntactic prior from dependency parses during pretraini…
- **Why it matters:** Positional embeddings (PE) in Transformers encode token distance and order but are largely agnostic to \textit{syntactic structure}. We introduce \textbf{S}yntax-\textbf{i}nformed \textbf{P}ositional \textbf{E}mbeddings (\textbf{SiPE}), which learns a lightweight syntactic prior from dependency parses during pretraini…
- **Tags:** cs.CL, cs.AI

### [The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images](https://arxiv.org/abs/2608.06270v1)

- **Authors:** Zhiheng Wang, Bo Peng, Lai Wei, Chaochao Lu
- **Source:** arXiv
- **Date:** 2026-08-07
- **One-sentence summary:** The "thinking-with-images" paradigm equips multimodal LLMs with active visual operations such as crop-and-zoom. However, models using these operations often achieve only marginal or negative gains over direct inference at substantially higher token cost.
- **Why it matters:** The "thinking-with-images" paradigm equips multimodal LLMs with active visual operations such as crop-and-zoom. However, models using these operations often achieve only marginal or negative gains over direct inference at substantially higher token cost.
- **Tags:** cs.AI

### [LLM Inference Under Bursty Workload Distribution: Modifying the WAIT Algorithm](https://arxiv.org/abs/2608.06135v1)

- **Authors:** Anjali Gangadhar Katageria, Shobha Rani, Raghu Nandan Sengupta
- **Source:** arXiv
- **Date:** 2026-08-06
- **One-sentence summary:** Large Language Models (LLMs) such as ChatGPT and Claude are widely used for information retrieval and problem-solving. Recent work has focused on improving scheduling algorithms to boost throughput while maintaining low latency.
- **Why it matters:** Large Language Models (LLMs) such as ChatGPT and Claude are widely used for information retrieval and problem-solving. Recent work has focused on improving scheduling algorithms to boost throughput while maintaining low latency.
- **Tags:** cs.LG

### [A Six-Dimensional Taxonomy of Post-Training Adaptation Techniques with Applications in AI Governance](https://arxiv.org/abs/2608.06246v1)

- **Authors:** Fardin Afdideh, Fernando Seoane, Farhad Abtahi
- **Source:** arXiv
- **Date:** 2026-08-07
- **One-sentence summary:** Post-training adaptation has become central to modern machine learning practice and includes techniques such as retraining, fine-tuning, parameter-efficient adaptation, alignment, retrieval augmentation, model editing, unlearning, calibration, and Multimodal Instruction Tuning. However, the literature remains fragment…
- **Why it matters:** Post-training adaptation has become central to modern machine learning practice and includes techniques such as retraining, fine-tuning, parameter-efficient adaptation, alignment, retrieval augmentation, model editing, unlearning, calibration, and Multimodal Instruction Tuning. However, the literature remains fragment…
- **Tags:** cs.LG

### [Tytan: Interactive Neurosymbolic Construction of Analytic Semantic Schemas from Relational Data](https://arxiv.org/abs/2608.06331v1)

- **Authors:** Donna Hooshmand, Shubham Shahi, Cameron Barrie, Abhratanu Dutta, Marko Sterbentz, Harper Pack, Kristian J. Hammond
- **Source:** arXiv
- **Date:** 2026-08-07
- **One-sentence summary:** From natural-language query interfaces to automated report generation, data analysis tools need a description of the data: the real-world entities it contains, which columns function as measures or identifiers, and how tables connect into units of analysis. Today, this semantic layer is usually written by hand.
- **Why it matters:** From natural-language query interfaces to automated report generation, data analysis tools need a description of the data: the real-world entities it contains, which columns function as measures or identifiers, and how tables connect into units of analysis. Today, this semantic layer is usually written by hand.
- **Tags:** cs.DB, cs.AI

## 2. Industry News

### [TutorMoments: Do AI tutors know when to help and when to hold back?](https://huggingface.co/blog/allenai/tutormoments)

- **Source:** Hugging Face Blog
- **Date:** 2026-08-08
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [Responding to the next frontier of critical cyber capabilities](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities)

- **Source:** OpenAI News
- **Date:** 2026-08-07
- **Summary:** OpenAI is sharing preliminary cybersecurity evaluations for Astra and the steps we’re taking to strengthen safeguards and security controls.
- **Impact:** OpenAI is sharing preliminary cybersecurity evaluations for Astra and the steps we’re taking to strengthen safeguards and security controls.

### [How HSP GRUPPE builds AI capabilities for tax advisory](https://openai.com/index/hsp-gruppe)

- **Source:** OpenAI News
- **Date:** 2026-08-07
- **Summary:** Discover how HSP GRUPPE uses ChatGPT Enterprise to boost productivity, improve work quality, and create more capacity for tax advisory and client service.
- **Impact:** Discover how HSP GRUPPE uses ChatGPT Enterprise to boost productivity, improve work quality, and create more capacity for tax advisory and client service.

### [Baseten on Hugging Face Inference Providers 🔥](https://huggingface.co/blog/baseten)

- **Source:** Hugging Face Blog
- **Date:** 2026-08-06
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [WeatherNext: AI model achieves breakthrough in forecasting cyclones](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/)

- **Source:** Google DeepMind Blog
- **Date:** 2026-08-06
- **Summary:** No summary was provided by the source.
- **Impact:** No summary was provided by the source.

### [Improving GPT‑5.6 Sol in ChatGPT—and expanding access to GPT-5.6 Luna for free users](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt)

- **Source:** OpenAI News
- **Date:** 2026-08-06
- **Summary:** ChatGPT introduces improved GPT-5.6 Sol with better accuracy and consistency, plus expanded access for free users and unlimited everyday chats with GPT-5.6 Luna.
- **Impact:** ChatGPT introduces improved GPT-5.6 Sol with better accuracy and consistency, plus expanded access for free users and unlimited everyday chats with GPT-5.6 Luna.

### [Working with the American Psychological Association on youth mental health and AI](https://openai.com/index/openai-and-apa-partner-to-advance-responsible-ai)

- **Source:** OpenAI News
- **Date:** 2026-08-06
- **Summary:** OpenAI and the American Psychological Association advance evidence-based guidance, resources, and safeguards for responsible AI use and youth mental health.
- **Impact:** OpenAI and the American Psychological Association advance evidence-based guidance, resources, and safeguards for responsible AI use and youth mental health.

### [From asking to doing: How the world is putting ChatGPT to work](https://openai.com/index/how-the-world-is-putting-chatgpt-to-work)

- **Source:** OpenAI News
- **Date:** 2026-08-06
- **Summary:** New OpenAI Signals data shows how people use ChatGPT worldwide, with country-level insights on adoption, usage trends, and evolving behavior.
- **Impact:** New OpenAI Signals data shows how people use ChatGPT worldwide, with country-level insights on adoption, usage trends, and evolving behavior.

## 3. Open Source Projects

### [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

- **Stars:** 34,821
- **Language:** Python
- **Updated date:** 2026-08-09
- **Summary:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码
- **Why it is useful:** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）开源主仓库：全书正文、编译版 PDF 与按章配套代码

### [langgenius/dify](https://github.com/langgenius/dify)

- **Stars:** 151,807
- **Language:** TypeScript
- **Updated date:** 2026-08-09
- **Summary:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.
- **Why it is useful:** Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without rebuilding the stack.

### [cactus-compute/cactus](https://github.com/cactus-compute/cactus)

- **Stars:** 5,566
- **Language:** C++
- **Updated date:** 2026-08-09
- **Summary:** Quantization, kernels, runtime and inference engine for mobiles, wearables, smart home and robots.
- **Why it is useful:** Quantization, kernels, runtime and inference engine for mobiles, wearables, smart home and robots.

### [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)

- **Stars:** 65,547
- **Language:** Python
- **Updated date:** 2026-08-09
- **Summary:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.
- **Why it is useful:** Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers.

### [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c)

- **Stars:** 3,827
- **Language:** C
- **Updated date:** 2026-08-08
- **Summary:** A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no framework, no GPU.
- **Why it is useful:** A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no framework, no GPU.

### [intel/auto-round](https://github.com/intel/auto-round)

- **Stars:** 1,559
- **Language:** Python
- **Updated date:** 2026-08-09
- **Summary:** A SOTA quantization algorithm for high-accuracy low-bit LLM inference, seamlessly optimized for CPU/XPU/CUDA, with multi-datatype support and full compatibility with vLLM, SGLang, and Transformers.
- **Why it is useful:** A SOTA quantization algorithm for high-accuracy low-bit LLM inference, seamlessly optimized for CPU/XPU/CUDA, with multi-datatype support and full compatibility with vLLM, SGLang, and Transformers.

### [deepset-ai/haystack](https://github.com/deepset-ai/haystack)

- **Stars:** 26,150
- **Language:** Python
- **Updated date:** 2026-08-08
- **Summary:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.
- **Why it is useful:** Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation.

### [infiniflow/ragflow](https://github.com/infiniflow/ragflow)

- **Stars:** 87,090
- **Language:** Go
- **Updated date:** 2026-08-08
- **Summary:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs
- **Why it is useful:** RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capabilities to create a superior context layer for LLMs

## 4. AI Accelerator & Hardware Trends

### [PaDoc: Layout-Grounded Parallel Decoding for Document Parsing](https://arxiv.org/abs/2608.06146v1)

- **Source:** arXiv
- **Date:** 2026-08-06
- **Summary:** End-to-end document parsers provide a unified interface, but serialize page layouts and regional contents into one autoregressive sequence. This formulation forces independent regions onto a decoding path whose length grows with the total content, whereas crop-based two-stage parsers expose region-level parallelism at…
- **Hardware relevance:** End-to-end document parsers provide a unified interface, but serialize page layouts and regional contents into one autoregressive sequence. This formulation forces independent regions onto a decoding path whose length grows with the total content, whereas crop-based two-stage parsers expose region-level parallelism at…
- **Keywords:** GPU

### [TS-RAG: Retrieval Augmented Generation for Time Series Forecasting](https://arxiv.org/abs/2608.06223v1)

- **Source:** arXiv
- **Date:** 2026-08-07
- **Summary:** While deep learning models, particularly transformer-based architectures, have shown impressive performance in time series forecasting, the application of retrieval-augmented generation (RAG) in this domain remains limited. Since RAG has proven effective in enhancing the capabilities of large language models by incorp…
- **Hardware relevance:** While deep learning models, particularly transformer-based architectures, have shown impressive performance in time series forecasting, the application of retrieval-augmented generation (RAG) in this domain remains limited. Since RAG has proven effective in enhancing the capabilities of large language models by incorp…
- **Keywords:** NPU

### [NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering](https://arxiv.org/abs/2608.06292v1)

- **Source:** arXiv
- **Date:** 2026-08-07
- **Summary:** Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely opaque: intermediate reasoning steps are difficult to verify and cannot be reliably attributed to specific evidence.
- **Hardware relevance:** Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely opaque: intermediate reasoning steps are difficult to verify and cannot be reliably attributed to specific evidence.
- **Keywords:** TPU

### [Beyond Sequence Order: Syntax-Informed Positional Embeddings for Transformers](https://arxiv.org/abs/2608.06111v1)

- **Source:** arXiv
- **Date:** 2026-08-06
- **Summary:** Positional embeddings (PE) in Transformers encode token distance and order but are largely agnostic to \textit{syntactic structure}. We introduce \textbf{S}yntax-\textbf{i}nformed \textbf{P}ositional \textbf{E}mbeddings (\textbf{SiPE}), which learns a lightweight syntactic prior from dependency parses during pretraini…
- **Hardware relevance:** Positional embeddings (PE) in Transformers encode token distance and order but are largely agnostic to \textit{syntactic structure}. We introduce \textbf{S}yntax-\textbf{i}nformed \textbf{P}ositional \textbf{E}mbeddings (\textbf{SiPE}), which learns a lightweight syntactic prior from dependency parses during pretraini…
- **Keywords:** NPU, ISCA

### [The Illusion of Visual Tool-Use: A Causal Audit of Thinking with Images](https://arxiv.org/abs/2608.06270v1)

- **Source:** arXiv
- **Date:** 2026-08-07
- **Summary:** The "thinking-with-images" paradigm equips multimodal LLMs with active visual operations such as crop-and-zoom. However, models using these operations often achieve only marginal or negative gains over direct inference at substantially higher token cost.
- **Hardware relevance:** The "thinking-with-images" paradigm equips multimodal LLMs with active visual operations such as crop-and-zoom. However, models using these operations often achieve only marginal or negative gains over direct inference at substantially higher token cost.
- **Keywords:** ISCA

### [BaKron: Efficient Quantization with Kronecker-Factored Hessians](https://arxiv.org/abs/2608.06291v1)

- **Source:** arXiv
- **Date:** 2026-08-07
- **Summary:** We accelerate a family of algorithms for neural network quantization whose geometry is informed by any Kronecker-factored approximation of the Hessian. GPTQ-style adaptive rounding typically uses one-sided information derived from input activations.
- **Hardware relevance:** We accelerate a family of algorithms for neural network quantization whose geometry is informed by any Kronecker-factored approximation of the Hessian. GPTQ-style adaptive rounding typically uses one-sided information derived from input activations.
- **Keywords:** TPU, NPU

### [HOPE: Hand-Object Pressure Estimation from Monocular Videos](https://arxiv.org/abs/2608.06192v1)

- **Source:** arXiv
- **Date:** 2026-08-06
- **Summary:** Estimating physical pressure from vision is essential for understanding contact-rich hand-object interaction. However, prior vision-based pressure estimation methods are largely limited to planar surfaces and single image input, making them difficult to apply to dynamic hand-object interaction with diverse objects.
- **Hardware relevance:** Estimating physical pressure from vision is essential for understanding contact-rich hand-object interaction. However, prior vision-based pressure estimation methods are largely limited to planar surfaces and single image input, making them difficult to apply to dynamic hand-object interaction with diverse objects.
- **Keywords:** TPU, NPU

### [BioKD: Selective Physiology-to-Video Knowledge Distillation via Reliability Gate for Emotion Recognition](https://arxiv.org/abs/2608.06023v1)

- **Source:** arXiv
- **Date:** 2026-08-06
- **Summary:** To address the limitations of video-based emotion recognition under ambiguous or socially masked behavioral cues, as well as the poor deployability of physiological signals, this paper proposes a reliability-aware physiology-to-video knowledge distillation framework, termed BioKD. The proposed framework leverages phys…
- **Hardware relevance:** To address the limitations of video-based emotion recognition under ambiguous or socially masked behavioral cues, as well as the poor deployability of physiological signals, this paper proposes a reliability-aware physiology-to-video knowledge distillation framework, termed BioKD. The proposed framework leverages phys…
- **Keywords:** NPU

## 5. What I Should Study Next

- inference
- LLM
- FPGA / ASIC accelerator architecture
- systolic arrays and dataflow
- quantized inference optimization

## 6. Suggested Reading Order

1. 先讀 Industry News，建立本週產業背景。
2. 接著瀏覽 Open Source Projects，動手理解工具與工作流。
3. 再讀 Top AI Papers，掌握方法、實驗與 benchmark。
4. 最後深入 AI Accelerator & Hardware Trends，串連架構、效能與系統限制。
