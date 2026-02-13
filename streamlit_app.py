import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Poly No-Lag", layout="wide")

st.title("🟢 Poly No-Lag Dashboard")
st.caption("15min scalps • Polymarket REST • Vancouver")

@st.cache_data(ttl=5)
def get_poly_data():
    try:
        r = requests.get("https://clob.polymarket.com/prices?limit=50")
        return pd.DataFrame(r.json())
    except:
        return pd.DataFrame()

df = get_poly_data()

col1, col2 = st.columns(2)

with col1:
    if not df.empty:
        st.metric("Markets", len(df))
        st.dataframe(df[['token_id', 'price']].tail(5))

with col2:
    if len(df) > 1:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df.index, 
            y=df.get('price', np.zeros(len(df))),
            mode='lines',
            name='Price'
        ))
        st.plotly_chart(fig, use_container_width=True)
