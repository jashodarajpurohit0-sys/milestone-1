# Downloads cryptocurrency price data using yfinance
# ----------------------------------------------------------

import yfinance as yf
import pandas as pd


def download_crypto_data(coin="BTC-USD", start="2018-01-01", end="2024-12-31"):
    """
    Function to download crypto data.
    Example coins: BTC-USD, ETH-USD, BNB-USD
    """

    print(f"\n📥 Downloading data for {coin} ...")

    df = yf.download(coin, start=start, end=end)

    if df.empty:
        print("❌ Error: No data found for the coin. Try another symbol.")
        return None

    print("✅ Download complete for {coin}. Showing first 5 rows:\n")
    print(df.head())

    return df
def download_all_coins():
    """downloads data for 5 major coins."""
    coins=["BTC-USD","ETH-USD","BNB-USD","ADA-USD","XRP-USD"]
    all_data={}
    for coin in coins:
        df=download_crypto_data(coin)
        if df is not None :
            all_data[coin]=df
    return all_data
if __name__=="__main__":
    download_crypto_data("BTC-USD")



