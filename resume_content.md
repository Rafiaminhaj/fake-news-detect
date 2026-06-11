# Professional Resume Content

Below is a beautifully structured, recruiter-ready resume content template that highlights your skills in Artificial Intelligence, NLP, Web Development, and cloud-computing platforms like **Google Colab**.

You can copy and paste this directly into your resume template (MS Word, Canva, or LaTeX).

---

## 🛠️ Technical Skills

* **Programming Languages:** Python, JavaScript (ES6+), HTML5, CSS3
* **Machine Learning & NLP:** Hugging Face `transformers` (BERT, Qwen, DistilBERT), PyTorch, LangChain, FAISS Vector Index, semantic Embeddings, Scikit-Learn, Pandas, NumPy, WordCloud
* **Developer Tools & Platforms:** **Google Colab (GPU Acceleration)**, Jupyter Notebooks, Git, GitHub, VS Code
* **Web Development:** Vanilla CSS, Responsive Layouts, Dynamic Charts (Chart.js), Web APIs (Flask/JSON REST APIs)

---

## 💻 Projects

### **PDF AI Assistant & Chatbot (RAG System)**
*Designed and implemented a Retrieval-Augmented Generation (RAG) system inside Google Colab to upload, index, and query PDF documents locally.*
* **Local GPU Inference:** Loaded and quantized the state-of-the-art `Qwen/Qwen2.5-1.5B-Instruct` model locally on **Google Colab's T4 GPU** using half-precision (`float16`) for rapid, cost-free inference.
* **Vector Indexing:** Utilized Hugging Face's `all-MiniLM-L6-v2` embedding model to encode text chunks and stored them in Facebook's `FAISS` vector engine for fast similarity search queries.
* **RAG Prompt Engineering:** Designed a structured context-retrieval pipeline that extracts relevant text chunks from PDFs and formats them inside prompt templates to eliminate model hallucinations.
* **Interactive Source-Reference UI:** Built an interactive chat widget using `ipywidgets` and custom HTML/CSS inside Google Colab, displaying generated AI answers alongside clickable source references.
* **Code Repository:** [GitHub - Rafiaminhaj/-pdf-ai-assistant](https://github.com/Rafiaminhaj/-pdf-ai-assistant)

---

### **Fake Indian News Detection System using Fine-Tuned BERT**
*Developed an end-to-end NLP sequence classification pipeline to detect fake news targeting the Indian media ecosystem.*
* **Hugging Face Fine-Tuning:** Fine-tuned a pre-trained `distilbert-base-uncased` transformer model using PyTorch and the Hugging Face `Trainer` API for binary classification.
* **Google Colab Cloud Execution:** Leveraged **Google Colab's T4 GPU** infrastructure to accelerate deep learning computation, optimizing training epochs and weights.
* **Dataset Engineering:** Programmatically generated a balanced dataset of 500 headlines covering Indian entities (ISRO, RBI, IPL, BCCI, Bollywood) to train the model.
* **EDA & Diagnostics:** Engineered side-by-side vocabulary WordClouds with stopword cleaning and plotted training/validation loss curves.
* **Interactive Client Widget:** Integrated a real-time web-style interactive widget using `ipywidgets` and HTML within Google Colab, allowing users to type custom headlines and receive color-coded confidence predictions.
* **Code Repository:** [GitHub - Rafiaminhaj/fake-news-detect](https://github.com/Rafiaminhaj/fake-news-detect)

---

### **Carbon Footprint Awareness Platform**
*Built a responsive, gamified web application to track carbon footprints, set goals, and drive sustainability awareness.*
* **Interactive Frontend:** Built a modern, dark-mode landing page using HTML5 and Vanilla CSS with custom micro-animations and responsive layouts.
* **Real-time Analytics:** Implemented dynamic data visualization using Chart.js to display breakdown categories (energy, diet, driving, transit) and compare scores to national averages.
* **AI Eco-Assistant Integration:** Embedded an interactive, context-aware chatbot widget that dynamically analyzes user emission profiles and recommends reduction strategies.
* **Gamification Features:** Designed a weekly target progress tracker that updates dynamically as users accept eco-pledges, awards Green Points (GP), and updates a global leaderboard.
