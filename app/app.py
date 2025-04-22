
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import calculate_ratios

st.set_page_config(page_title="Financial Statement Analyzer", layout="wide")
st.title("📊 Financial Statement Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    if "Year" not in df.columns:
        st.error("CSV must contain a 'Year' column.")
    else:
        df.set_index("Year", inplace=True)
        df = df.sort_index(ascending=True)
        df = calculate_ratios(df)
        
        st.subheader("📈 Key Financial Ratios")
        ratio_columns = [
            "Gross_Margin", "Net_Margin", "ROE", "ROA",
            "Current_Ratio", "Quick_Ratio", "Debt_to_Equity", "Interest_Coverage"
        ]
        st.dataframe(df[ratio_columns].style.format("{:.2f}"))

        # Plotting
        st.subheader("📊 Ratio Trends Over Time")
        selected_ratios = st.multiselect("Select ratios to plot", ratio_columns, default=ratio_columns[:3])
        
        if selected_ratios:
            fig, ax = plt.subplots(figsize=(12, 5))
            df[selected_ratios].plot(marker="o", ax=ax)
            plt.title("Financial Ratios Over Time")
            plt.xlabel("Year")
            plt.ylabel("Ratio Value")
            plt.grid(True)
            st.pyplot(fig)
