Here's a comprehensive README.md for the Content Engine repository:

```markdown
# Content Engine - 10-K Document Analysis

A powerful document analysis system that uses local LLMs and embeddings to analyze and compare Form 10-K filings. Built with privacy-first approach using fully local models.

## Features

- 📄 Analyze multiple Form 10-K documents simultaneously
- 🔍 Advanced semantic search and comparison
- 💬 Interactive chat interface for document queries
- 📊 Side-by-side document comparison
- 🔒 Fully local processing - no data leaves your machine
- 📈 Visual comparison of key metrics
- ⚡ Real-time document processing

## Architecture

The system is built using:
- **Backend Framework**: LangChain for document processing and LLM integration
- **Frontend**: Streamlit for the user interface
- **Vector Store**: ChromaDB for efficient document retrieval
- **Embedding Model**: Sentence Transformers (all-MiniLM-L6-v2)
- **LLM**: Llama 2 7B Chat (Quantized version)

## Project Structure

```
content-engine/
├── app/
│   ├── components/
│   │   ├── chat.py           # Chat interface component
│   │   ├── comparison.py     # Document comparison view
│   │   ├── document_viewer.py # Document viewing component
│   │   └── sidebar.py        # Settings sidebar
│   └── main.py               # Main Streamlit application
├── engine/
│   ├── document.py           # Document processing
│   ├── embeddings.py         # Local embedding model
│   ├── llm.py               # Local LLM integration
│   ├── store.py             # Vector store operations
│   └── __init__.py          # Engine initialization
├── data/
│   └── pdfs/                # PDF documents
├── models/
│   ├── embeddings/          # Embedding model files
│   └── llm/                 # LLM model files
└── requirements.txt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/content-engine.git
cd content-engine
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download required models:
- Follow instructions in `models/README.md` to download the LLM
- Embedding model will be downloaded automatically on first run

5. Place your Form 10-K documents in `data/pdfs/`

## Usage

1. Start the application:
```bash
streamlit run app/main.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Use the interface to:
- Select documents for analysis
- Ask questions about the documents
- Compare different sections
- View source information

## Example Queries

The system can answer questions like:
- "What are the risk factors associated with Google and Tesla?"
- "What is the total revenue for Google Search?"
- "What are the differences in the business of Tesla and Uber?"
- "Compare the financial metrics of all companies"

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Requirements

- Python 3.8+
- 16GB+ RAM recommended
- 10GB+ disk space for models
- CUDA-capable GPU optional but recommended

## Dependencies

Key dependencies include:
- streamlit==1.24.0
- sentence-transformers==2.2.2
- chromadb==0.4.3
- llama-cpp-python==0.1.77
- PyMuPDF==1.22.5
- numpy==1.24.3

## Privacy

All processing is done locally:
- No data is sent to external services
- Models run entirely on your machine
- Document analysis is completely private

## License

MIT License - See LICENSE file for details

## Acknowledgments

- LlamaIndex and LangChain for document processing frameworks
- Hugging Face for model distributions
- Streamlit for the UI framework