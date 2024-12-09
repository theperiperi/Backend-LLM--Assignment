from pathlib import Path
from typing import Dict, Optional
from .document import DocumentProcessor
from .embeddings import LocalEmbeddings
from .store import VectorStore
from .llm import LocalLLM

class Engine:
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.doc_processor = DocumentProcessor()
        self.embeddings = LocalEmbeddings()
        self.vector_store = VectorStore()
        self.llm = LocalLLM()
        
    def initialize(self):
        """Initialize the engine and process documents"""
        # Create collections
        self.vector_store.create_collection("10k_docs")
        
        # Process and index documents
        docs_path = Path(self.config.get("docs_dir", "data/pdfs"))
        for pdf_file in docs_path.glob("*.pdf"):
            # Load and process document
            text = self.doc_processor.load_pdf(pdf_file.name)
            chunks = self.doc_processor.chunk_text(text)
            
            # Generate embeddings
            chunk_embeddings = self.embeddings.embed_batch(chunks)
            
            # Add to vector store
            self.vector_store.add_documents(
                "10k_docs",
                chunks,
                chunk_embeddings,
                [{"source": pdf_file.name, "section": self._detect_section(chunk)} 
                 for chunk in chunks]
            )
    
    def _detect_section(self, text: str) -> str:
        """Detect the section of the document based on content"""
        text_lower = text.lower()
        if "risk factors" in text_lower:
            return "Risk Factors"
        elif "management's discussion" in text_lower:
            return "MD&A"
        elif "business" in text_lower:
            return "Business Overview"
        else:
            return "Other"
            
    def query(self, question: str) -> Dict:
        """Process a query and return response with context"""
        # Get relevant context
        results = self.vector_store.query("10k_docs", question)
        context = "\n".join(results["documents"][0])
        
        # Generate response
        response = self.llm.generate_response(question, context)
        
        return {
            "response": response,
            "context": results
        } 