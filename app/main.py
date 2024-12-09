import streamlit as st
from engine import Engine
from components.sidebar import render_sidebar
from components.chat import render_chat_interface
from components.document_viewer import render_document_viewer
from components.comparison import render_comparison_view

def main():
    st.title("10-K Document Analysis Engine")
    
    # Initialize engine
    if "engine" not in st.session_state:
        st.session_state.engine = Engine()
        st.session_state.engine.initialize()
    
    # Render sidebar
    settings = render_sidebar()
    
    # Render chat interface
    if prompt := render_chat_interface():
        # Process query
        result = st.session_state.engine.query(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(result["response"])
        
        # Add assistant response to chat history
        st.session_state.messages.append({
            "role": "assistant",
            "content": result["response"]
        })
        
        # Show source documents
        render_document_viewer(result["context"])
    
    # Render comparison view if multiple documents are selected
    if len(settings["selected_docs"]) > 1:
        render_comparison_view({
            "metrics": st.session_state.engine.get_metrics_comparison(),
            "risks": st.session_state.engine.get_risk_comparison(),
            "business": st.session_state.engine.get_business_comparison()
        })

if __name__ == "__main__":
    main() 