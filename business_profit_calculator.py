import plotly.express as px
import pandas as pd
import streamlit as st
import logging
import warnings

st.set_page_config(page_title="Business Profit Simulator", layout="wide")

@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    data["Date"] = pd.to_datetime(data["Date"], format='%Y')
    return data

df = load_data("Py.csv")
df = df.select_dtypes(exclude=["category", "object"])

st.title("Business Profit & Tax Simulator")

with st.sidebar:
    st.header("Simulation Settings")
    
    min_year  = int(df["Date"].dt.year.min())
    max_year = int(df["Date"].dt.year.max())
    date_range = st.slider("Analysis Period", min_year, max_year, (min_year, max_year))
    
    markup_perc = st.slider("MarkUp Rate (%)", -100, 1000, 100)
    tax_rate = st.slider("Product Tax (%)", 0, 100, 20)
    net_tax_perc = st.slider("Net Profit Tax (%)", 0, 100, 25)
    
    st.subheader("Display Options")
    round_up = st.checkbox("Round Prices")
    make_spline = st.checkbox("Smooth Charts (Spline)")

mask = (df["Date"].dt.year >= date_range[0]) & (df["Date"].dt.year <= date_range[1])
df_filtered = df.loc[mask].copy()

df_filtered["Price"] = (df_filtered["Cost"] * (1 + markup_perc/100)) * (1 + tax_rate/100)

if round_up:
    df_filtered["Price"] = df_filtered["Price"].round()

df_filtered["profit_per_product"] = (df_filtered["Price"] / (1 + tax_rate/100) - df_filtered["Cost"])
df_filtered["gross_profit"] = df_filtered["profit_per_product"] * df_filtered["Sales"]
df_filtered["tax_amount"] = df_filtered["gross_profit"] * (net_tax_perc / 100)
df_filtered["net_profit"] = df_filtered["gross_profit"] - df_filtered["tax_amount"]

m1, m2, m3 = st.columns(3)
m1.metric("Total Sales Volume", f"{df_filtered['Sales'].sum()}")
m2.metric("Total Net Profit", f"${df_filtered['net_profit'].sum()}")
m3.metric("Tax Liability", f"${df_filtered['tax_amount'].sum()}")

line_shape = "spline" if make_spline else "linear"

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Price vs Cost Trend")
    fig_line = px.line(df_filtered, x="Date", y=["Cost", "Price"], markers=True, line_shape=line_shape, title="Price Evolution")
    fig_line.data[1].update(fill='tonexty', fillcolor='rgba(0, 255, 0, 0.1)')
    st.plotly_chart(fig_line, width="stretch")

with col_right:
    st.subheader("Profit and tax Breakdown")
    fig_bar = px.bar(df_filtered, x="Date", y=["net_profit", "tax_amount"], title="Net Profit vs Tax")
    st.plotly_chart(fig_bar, width="stretch")

st.divider()

c1, c2 = st.columns([2, 1])

with c1:
    st.subheader("Detailed Comparison")
    fig_multi = px.bar(df_filtered, x="Date", y=["Cost", "Price", "profit_per_product"], barmode="group")
    st.plotly_chart(fig_multi, width="stretch")

with c2:
    st.subheader("Feature Correlation")
    numeric_df = df_filtered.select_dtypes(exclude=["object", "datetime"])
    corr_mat = numeric_df.corr()
    fig_heat = px.imshow(corr_mat, text_auto=".2f", color_continuous_scale="RdBu_r")
    st.plotly_chart(fig_heat, width="stretch")
