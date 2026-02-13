import streamlit as st
import websocket
import json
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import threading
import time
import requests

st.set_page_config(layout="wide", page_title="Poly No-Lag")
st.title("🚀 Polymarket No-Lag Dashboard")

if "prices_poly" not in st.session
