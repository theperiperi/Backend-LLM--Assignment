# Model Files

This directory contains the required model files for the Content Engine.

## Required Models

### LLM Model
Download the Llama 2 7B Chat model (quantized version):
1. Visit [TheBloke's Hugging Face page](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)
2. Download the `llama-2-7b-chat.Q4_K_M.gguf` file
3. Place it in the `models/llm` directory
4. Rename it to `llama-2-7b-chat.gguf`

### Embedding Model
The sentence-transformers model will be automatically downloaded when first run:
- Model: `all-MiniLM-L6-v2`
- Location: `models/embeddings`

## Model Versions

- LLM: Llama 2 7B Chat (GGUF format)
- Embeddings: all-MiniLM-L6-v2

## Notes

- The LLM model is quantized for efficient CPU inference
- Models are not included in the repository due to size constraints
- All models run locally for data privacy 