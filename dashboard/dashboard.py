import streamlit as st
import pandas as pd

st.title("SentinelScope Dashboard")

logs = pd.read_csv("data/sample_logs.csv")

st.dataframe(logs)

st.bar_chart(logs['status'].value_counts())
