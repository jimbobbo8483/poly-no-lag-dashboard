import streamlit as st
import streamlit_websocket as ws
import json
import pandas as pd
from datetime import datetime

st.title("Poly No-Lag")

if "prices" not in st.session_state:
    st.session_state.prices
