# RAG-Powered-YT-Summarizer

An intelligent Retrieval-Augmented Generation (RAG) tool that allows you to "talk" to YouTube videos. This project supports both local LLMs (via Ollama) for privacy and Cloud APIs for multilingual summaries.

## 🚀 Features

- **Local LLM Integration:** Use deepseek-r1:8b or other local models via Ollama for private processing.

- **Multilingual Summaries:** Support for English and Hindi summaries (via app.py).

- **Seamless Transcript Fetching:** Automatic extraction of transcripts using youtube_transcript_api.

- **Dual Mode:** Choose between a lightweight local setup or a high-performance API-based setup.

## 📂 Project Structure

- `local_app.py`: Logic for local LLM integration (English only).

- `app.py`: API-driven version supporting English and Hindi summaries.

- `requirements.txt`: Python dependencies.

- `.gitignore`: Configuration to keep your environment and keys private.

## 🛠 Setup Instructions

Follow these steps to get the project running on your local machine.

1. **Environment Setup**

It is highly recommended to use `Conda` to manage dependencies. If the VS Code terminal gives you trouble, please use the Anaconda Prompt.

```Bash

# Open Anaconda Prompt and navigate to your drive (if necessary)
D:

# Navigate to your project folder
cd path/to/your/RAG-Integration-with-Youtube

# Create a new environment
conda create -n yt_rag python=3.10 -y

# Activate the environment
conda activate yt_rag

```

2. **Install Dependencies**

Once the environment is active, install the required libraries:

```bash

pip install -r requirements.txt
```

3. **Local LLM Configuration (For local_app.py)**

This project uses Ollama to run models locally.

1. Download and install `Ollama`.

2. Pull the DeepSeek model:

```bash
ollama run deepseek-r1:8b
```

## 💻 Usage

### **Option A:** Local Processing (*local_app.py*)

- Best for privacy and English-based querying.

- `python local_app.py`

### **Option B:** API-Based Summarization (*app.py*)

- Best for high-quality summaries in Hindi or English. Make sure to add your API Key in the .env file or as an environment variable.

- `python app.py`

## 🚀 App Demo

Experience the tool in action! You can try the bilingual summarizer and RAG interface via the deployed link below:

### ❗CAUTION

**Technical Note on Deployment:** Due to high request volumes, YouTube may occasionally block Cloud-based requests (Rate Limiting). If the demo link fails to fetch a transcript, it is likely a temporary IP block from YouTube. For a guaranteed experience, please follow the **Local Setup** instructions below.

**🔗 [Live Demo Link](https://rag-powered-yt-summarizer-vkhq8jr2sr6dde6xmjcfky.streamlit.app/)**

> **Note:** The local RAG features (Ollama) are only available when running the project on your machine. The deployed version uses Cloud APIs to demonstrate the bilingual summarization capabilities.

## ⚠️ Troubleshooting

- **Terminal Issues:** If `conda` is not recognized in VS Code, ensure your Python Path is set correctly or stick to the Anaconda Prompt.

- **Transcript Errors:** Some YouTube videos have disabled captions. This tool requires videos with available transcripts.

- **Ollama Connection:** Ensure the Ollama service is running in the background before launching `local_app.py`.

## 🤝 Contributing

Feel free to fork this repo, open issues, or submit pull requests to improve the RAG performance or add more language supports!

