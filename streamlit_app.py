import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import time
import numpy as np

st.title("🟢 Poly No-Lag Dashboard")

# Poly API - public markets
@st.cache_data(ttl=10)
def get_poly_markets():
    try:
        url = "https://clob.polymarket.com/markets?active=true&limit=20"
        r
