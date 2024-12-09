import chromadb
from chromadb.config import Settings
from typing import List, Dict

class VectorStore:
    def __init__(self, persist_dir: str = "data/chroma"):
        self.client = chromadb.Client(Settings(
            persist_directory=persist_dir,
            anonymized_telemetry=False
        ))
        
    def create_collection(self, name: str):
        """Create or get a collection"""
        return self.client.create_collection(name)
        
    def add_documents(self, collection_name: str, texts: List[str], 
                     embeddings: List[List[float]], metadata: List[Dict]):
        """Add documents to collection"""
        collection = self.client.get_collection(collection_name)
        collection.add(
            embeddings=embeddings,
            documents=texts,
            metadatas=metadata,
            ids=[f"doc_{i}" for i in range(len(texts))]
        )
        
    def query(self, collection_name: str, query_text: str, n_results: int = 5):
        """Query the vector store"""
        collection = self.client.get_collection(collection_name)
        results = collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results 