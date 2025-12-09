# ----------------------------------------------------------
# DATASET CREATION FOR MULTIPLE CRYPTOCURRENCIES
# ----------------------------------------------------------

import numpy as np

def create_dataset(df, window_size=20):
    """
    Converts closing prices into time-series sequences.
    """
    print("\n📦 Creating dataset ...")

    X, y = [], []
    close_prices = df["Close"].values

    for i in range(window_size, len(close_prices)):
        X.append(close_prices[i-window_size:i])
        y.append(close_prices[i])

    X, y = np.array(X), np.array(y)

    print(f"✅ Dataset created: X={X.shape}, y={y.shape}")
    return X, y


def create_all_datasets(preprocessed_data, window_size=20):
    """
    Creates datasets for all 5 coins.
    """
    all_datasets = {}

    for coin, df in preprocessed_data.items():
        print(f"\n====================================")
        print(f"📦 CREATING DATASET FOR {coin}")
        print("====================================")

        X, y = create_dataset(df, window_size)
        all_datasets[coin] = (X, y)

    return all_datasets
