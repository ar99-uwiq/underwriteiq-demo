
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="UnderwriteIQ Demo",
    page_icon="📊",
    layout="centered"
)

st.markdown(
    "<h1 style='text-align: center; color: #002c54;'>UnderwriteIQ</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center; color: #4c6c88;'>AI-Powered Financial Risk Advisor for Insurance Underwriting</h3>",
    unsafe_allow_html=True
)

st.write("")

st.markdown("### Upload Financial Statements")
st.write("Upload the balance sheet, income statement, cash flow, and notes for analysis.")

uploaded_files = st.file_uploader("Upload CSV or TXT files", accept_multiple_files=True, type=["csv", "txt"])

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully.")

st.markdown("---")

st.markdown("#### 📌 Features")
st.markdown("- Upload and review annual financial packages (2023 & 2024)")
st.markdown("- Automatic comparison to industry benchmarks")
st.markdown("- Risk ratio calculation and red flag detection")
st.markdown("- GPT-powered underwriting memo generation")
st.markdown("- Renewal tracking and historical comparison")

st.markdown("---")

st.markdown("##### 🚨 This is a *demo-only* version. All data and outputs are fictional and for demonstration purposes only.", unsafe_allow_html=True)
