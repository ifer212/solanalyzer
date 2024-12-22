import pandas as pd
import streamlit as st

def display_dashboard(df):
    st.title("Solana Trading Dashboard")
    st.write(df)
    st.bar_chart(df["pnl"])
