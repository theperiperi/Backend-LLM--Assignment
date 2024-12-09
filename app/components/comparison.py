import streamlit as st
import pandas as pd

def render_comparison_view(docs_data):
    """Render comparison view of documents"""
    st.subheader("Document Comparison")
    
    # Create tabs for different comparison views
    tabs = st.tabs(["Key Metrics", "Risk Factors", "Business Overview"])
    
    with tabs[0]:
        # Display key metrics comparison
        if docs_data.get("metrics"):
            df = pd.DataFrame(docs_data["metrics"])
            st.dataframe(df)
            
    with tabs[1]:
        # Display risk factors comparison
        if docs_data.get("risks"):
            for company, risks in docs_data["risks"].items():
                st.markdown(f"**{company} Risk Factors:**")
                for risk in risks:
                    st.markdown(f"- {risk}")
                    
    with tabs[2]:
        # Display business overview comparison
        if docs_data.get("business"):
            cols = st.columns(len(docs_data["business"]))
            for col, (company, overview) in zip(cols, docs_data["business"].items()):
                with col:
                    st.markdown(f"**{company}**")
                    st.markdown(overview) 