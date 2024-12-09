from typing import List
import fitz  # PyMuPDF
from pathlib import Path

class DocumentProcessor:
    def __init__(self, docs_dir: str = "data/pdfs"):
        self.docs_dir = Path(docs_dir)
        
    def load_pdf(self, filename: str) -> str:
        """Load and extract text from a PDF file"""
        doc = fitz.open(self.docs_dir / filename)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
        
    def chunk_text(self, text: str, chunk_size: int = 1000) -> List[str]:
        """Split text into chunks for processing"""
        chunks = []
        words = text.split()
        current_chunk = []
        current_size = 0
        
        for word in words:
            current_chunk.append(word)
            current_size += len(word) + 1
            
            if current_size >= chunk_size:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                current_size = 0
                
        if current_chunk:
            chunks.append(" ".join(current_chunk))
            
        return chunks 