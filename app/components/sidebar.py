import streamlit as st

def render_sidebar():
    """Render the sidebar with document selection and settings"""
    with st.sidebar:
        st.header("Settings")
        
        # Document selection
        selected_docs = st.multiselect(
            "Select documents to analyze",
            ["google-10k.pdf", "tesla-10k.pdf", "uber-10k.pdf"],
            default=["google-10k.pdf", "tesla-10k.pdf", "uber-10k.pdf"]
        )
        
        # Model settings
        st.subheader("Model Settings")
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
        max_tokens = st.slider("Max Response Length", 100, 1000, 512)
        
        return {
            "selected_docs": selected_docs,
            "temperature": temperature,
            "max_tokens": max_tokens
        } 