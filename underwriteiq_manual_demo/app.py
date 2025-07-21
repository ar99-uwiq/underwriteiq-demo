
import streamlit as st
import pandas as pd

st.set_page_config(page_title="UnderwriteIQ", layout="wide")

st.title("📊 UnderwriteIQ – AI-Enhanced Underwriting Demo")

st.markdown("Upload two years of financials to compare metrics, identify red flags, and generate a sample underwriting memo.")

uploaded_2023 = st.file_uploader("Upload 2023 Financials", type="csv")
uploaded_2024 = st.file_uploader("Upload 2024 Financials", type="csv")

if uploaded_2023 and uploaded_2024:
    df_2023 = pd.read_csv(uploaded_2023)
    df_2024 = pd.read_csv(uploaded_2024)

    st.subheader("📈 Year-over-Year Comparison")
    st.dataframe(pd.concat([df_2023, df_2024]))

    st.subheader("🚩 Red Flag Detection")
    red_flags = []
    if df_2024['Current_Ratio'][0] < 1.0:
        red_flags.append("Current Ratio below 1.0")
    if df_2024['Debt_to_Equity'][0] > 3.0:
        red_flags.append("High Debt-to-Equity Ratio")
    if df_2024['Net_Income'][0] < 0:
        red_flags.append("Negative Net Income")

    if red_flags:
        st.error("Red Flags:")
        for flag in red_flags:
            st.markdown(f"- {flag}")
    else:
        st.success("No red flags detected.")

    st.subheader("📝 Sample GPT-Based Underwriting Memo")
    st.text_area("Memo", value=f"This applicant shows stable financials. Red flags include: {', '.join(red_flags) if red_flags else 'None'}.")
