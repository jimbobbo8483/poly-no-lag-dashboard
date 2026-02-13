# 🚀 Poly No-Lag Dashboard - BTC RTDS Live

A high-performance, low-latency Streamlit dashboard for real-time BTC price streaming from Polymarket's CLOB (Central Limit Order Book).

## 🎯 Problem Solved

Traditional UI dashboards suffer from lag between what market makers and bots see versus what regular traders observe. This dashboard connects directly to Polymarket's WebSocket feed for minimal latency price updates.

## ✨ Features

- **Real-Time WebSocket Feed**: Direct connection to Polymarket CLOB for sub-second latency
- **Live Price Updates**: See BTC prices as they update across the network
- **Connection Status Indicator**: Know when you're connected and receiving data
- **Price Change Tracking**: Monitor momentum with +/- price indicators
- **Historical Price Chart**: Interactive Plotly chart with 500-point rolling window
- **Live Statistics**: Mean, standard deviation, min/max prices
- **Automatic Reconnection**: Handles connection drops gracefully
- **Thread-Safe Queue Processing**: Non-blocking background data collection
- **Dark Theme Optimized**: Easy on the eyes for extended monitoring

## 📋 Requirements

- Python 3.8+
- Streamlit 1.28.1+
- WebSocket client for real-time data
- Pandas for data processing
- Plotly for interactive charts

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

### 3. Monitor Live Data

The dashboard will:
- Connect to Polymarket's CLOB WebSocket
- Subscribe to BTC market feeds
- Display real-time price updates
- Show connection status and statistics

## 📊 Dashboard Components

### Top Metrics Row
- **Current BTC Price**: Latest price with change indicator
- **Connection Status**: 🟢 Connected or 🔴 Disconnected
- **Data Points**: Number of price updates collected
- **Range**: Highest and lowest prices in current session

### Main Chart
Interactive Plotly chart showing:
- Price timeline
- Hover details for each data point
- Zoom and pan capabilities
- Dark theme for extended viewing

### Statistics Table
- **Mean**: Average price across all data points
- **Std Dev**: Price volatility measurement
- **Min/Max**: Range of prices observed
- **Latest**: Most recent price

## 🔧 Configuration

Edit these variables in `app.py` to customize:

```python
POLYMARKET_WS_URL = "wss://clob.polymarket.com/ws"  # WebSocket endpoint
MAX_PRICE_HISTORY = 500                              # Data points to keep
RECONNECT_INTERVAL = 5                               # Seconds between reconnect attempts
```

## 📈 Performance Optimization

The dashboard is optimized for low-latency performance:

- **Background Threading**: WebSocket runs in separate thread, never blocking UI
- **Queue-Based Updates**: Thread-safe message queue for data processing
- **Circular Buffer**: Efficient deque auto-trims old data
- **Minimal Reruns**: Only refreshes when necessary
- **Streamlit Config**: Optimized settings in `.streamlit/config.toml`

## 🐛 Troubleshooting

### Dashboard shows "Loading..." but no prices appear
1. Check your internet connection
2. Verify Polymarket's CLOB is running: https://clob.polymarket.com
3. Check console for WebSocket errors
4. Try restarting the app

### Connection keeps dropping
- The dashboard has auto-reconnect enabled (5-second intervals)
- Check if your network has firewall restrictions on WebSocket connections
- Try connecting from a different network

### Prices seem delayed
- Streamlit reruns happen every 0.5 seconds minimum
- For even lower latency, consider using raw WebSocket with async/await
- Ensure you're not running other heavy processes

## 🚀 Advanced Features (Coming Soon)

- Order flow detection (identify bot activity)
- Price alerts and notifications
- Historical data export
- Multiple market tracking
- Performance metrics dashboard

## 📝 Technical Architecture

```
┌─────────────────────────────────────────────────────┐
│          Streamlit Web Interface                     │
└─────────────────────────────────────────────────────┘
                    ▲
                    │ st.session_state
                    │
┌─────────────────────────────────────────────────────┐
│       Message Queue (Thread-Safe)                    │
└─────────────────────────────────────────────────────┘
                    ▲
                    │
┌─────────────────────────────────────────────────────┐
│  WebSocket Thread (Background)                       │
└─────────────────────────────────────────────────────┘
                    ▲
                    │ JSON messages
                    │
         ┌─��────────┴──────────┐
         │                     │
    WebSocket CLOB API    Reconnection Handler
    (Polymarket)
```

## 📚 Resources

- [Polymarket CLOB Documentation](https://docs.polymarket.com)
- [Streamlit Documentation](https://docs.streamlit.io)
- [WebSocket Documentation](https://python-websockets.readthedocs.io/)

## 📝 License

Open source - feel free to modify and use

## 🤝 Contributing

Found a bug or have an idea? Open an issue or submit a PR!

---

Built with ❤️ for traders who want to stay ahead of the lag
