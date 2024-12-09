from llama_cpp import Llama
from typing import Dict

class LocalLLM:
    def __init__(self, model_path: str = "models/llama-2-7b-chat.gguf"):
        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4
        )
        
    def generate_response(self, prompt: str, context: str) -> str:
        """Generate response using local LLM"""
        full_prompt = f"""Context: {context}
        
        Question: {prompt}
        
        Answer based on the context above:"""
        
        response = self.llm(
            full_prompt,
            max_tokens=512,
            temperature=0.7,
            stop=["Question:", "\n\n"]
        )
        
        return response["choices"][0]["text"].strip() 