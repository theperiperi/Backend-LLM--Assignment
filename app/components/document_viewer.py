import streamlit as st

def render_document_viewer(results):
    """Render the document viewer with source information"""
    with st.expander("View Source Documents"):
        tabs = st.tabs(["Source " + str(i+1) for i in range(len(results["documents"][0]))])
        
        for tab, doc, metadata in zip(tabs, results["documents"][0], results["metadatas"][0]):
            with tab:
                st.markdown(f"**Source**: {metadata['source']}")
                st.markdown(f"**Section**: {metadata.get('section', 'N/A')}")
                st.markdown("**Content**:")
                st.markdown(doc) 