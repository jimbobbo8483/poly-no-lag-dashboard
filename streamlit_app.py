import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Poly No-Lag", layout="wide")

st.title("🟢 Poly No-Lag")
st.caption("Polymarket Live • 15min Scalps")

@st.cache_data(ttl=5)
def get_poly_data():
    try:
        r = requests.get("https://clob.polymarket.com/markets?active=true&limit=20")
        data = r.json()
        df = pd.json_normalize(data)
        return df[['question', 'yes_price', 'no_price', 'volume_24h']].tail(10)
    except:
        return pd.DataFrame()

df = get_poly_data()

col1, col2 = st.columns(2)

with col1:
    if not df.empty:
        st.metric("Live Markets", len(df))
        st.dataframe(df, use_container_width=True)

with col2:
    if not df.empty and 'yes_price' in df.columns:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df['yes_price'], 
                                mode='lines+markers', name='Yes $',
                                line=dict(color='#10B981')))
        fig.add_trace(go.Scatter(x=df.index, y=df['no_price'], 
                                mode='lines+markers', name='No $',
                                line=dict(color='#EF4444')))
        st.plotly_chart(fig, use_container_width=True)
