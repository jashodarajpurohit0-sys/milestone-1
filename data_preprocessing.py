# ----------------------------------------------------------
# DATA PREPROCESSING FOR MULTIPLE CRYPTOCURRENCIES
# ----------------------------------------------------------

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_single(df):
    """
    Cleans & scales a single dataframe.
    """
    print("\n🛠 Starting preprocessing...")

    df = df.reset_index()

    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    df = df.fillna(method='ffill')

    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]

    scaler = MinMaxScaler()

    df_scaled = df.copy()
    df_scaled[["Open", "High", "Low", "Close", "Volume"]] = scaler.fit_transform(
        df_scaled[["Open", "High", "Low", "Close", "Volume"]]
    )

    print("✅ Preprocessing complete. First 5 rows:")
    print(df_scaled.head())

    return df_scaled, scaler


def preprocess_all(all_data):
    """
    Preprocess data for all 5 coins.
    """
    preprocessed = {}
    scalers = {}

    for coin, df in all_data.items():
        print(f"\n====================================")
        print(f"🧹 PREPROCESSING DATA FOR {coin}")
        print("====================================")
        
        clean_df, scaler = preprocess_single(df)

        preprocessed[coin] = clean_df
        scalers[coin] = scaler

    return preprocessed, scalers
