import yfinance as yf


data = yf.download("MSFT", start="2023-01-01", end="2024-01-01")


data_2 = yf.download("MSFT", period="1mo", interval="5m")