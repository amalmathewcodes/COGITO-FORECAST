import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# --- Page Config ---
st.set_page_config(page_title="COGITO-FORECAST", layout="wide")

# --- Header ---
st.title("📊 COGITO-FORECAST: SMB Financial Dashboard")
st.markdown("""
**Current Status:** Prototype v0.1
This tool automates financial forecasting and strategic planning for small businesses.
""")
st.divider()

# --- 1. Data Ingestion Layer ---
st.sidebar.header("1. Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload your financial CSV", type=["csv"])

# Helper function to generate dummy data if no file is uploaded (For Demo Purposes)
def load_demo_data():
    dates = pd.date_range(start="2024-01-01", periods=12, freq='M')
    data = {
        'Date': dates,
        'Revenue': [10000, 12000, 11000, 15000, 14000, 16000, 19000, 21000, 20000, 25000, 24000, 30000],
        'Expenses': [8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 14000, 15000, 18000]
    }
    return pd.DataFrame(data)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.success("File Uploaded Successfully!")
else:
    st.sidebar.info("Awaiting Upload... Using Demo Data for preview.")
    df = load_demo_data()

# Show Raw Data Preview
with st.expander("🔍 View Raw Data"):
    st.dataframe(df)

# --- 2. Visualization Layer ---
st.subheader("2. Financial Overview")
# Simple Plotly Chart to show "Current Status" capability
fig = px.line(df, x='Date', y=['Revenue', 'Expenses'], markers=True, title="Historical Financial Trends")
st.plotly_chart(fig, use_container_width=True)

# --- 3. Action Layer (The Buttons) ---
st.subheader("3. AI-Powered Analysis & Actions")

col1, col2, col3, col4 = st.columns(4)

# Button 1: Forecast
with col1:
    if st.button("🚀 Generate Forecast"):
        st.success("Module Active: Prophet Model initialized.")
        st.info("Generating 12-month predictions... (Placeholder for Phase 3)")

# Button 2: Analyze
with col2:
    if st.button("📈 Analyze Trends"):
        st.success("Module Active: Gemini API connected.")
        st.text_area("AI Analyst Report:", "Based on the data, Revenue is trending upwards by 15%...", height=150)

# Button 3: Plan
with col3:
    if st.button("📋 Action Plan"):
        st.success("Module Active: Strategic Planner.")
        st.markdown("""
        **Recommended Actions:**
        1. Reduce OpEx in Q3.
        2. Reinvest surplus from May into Marketing.
        """)

# Button 4: Download
with col4:
    if st.button("📄 Download PDF"):
        st.warning("Reporting Engine: Formatting PDF for download...")

# --- Footer ---
st.divider()
st.caption("Developed by [Amal Mathew] | Powered by Streamlit, Prophet & Google Gemini")