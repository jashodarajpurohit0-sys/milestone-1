
# ----------------------------------------------------------

import matplotlib.pyplot as plt

def plot_close_price(df,coin):
    plt.figure(figsize=(10,5))
    plt.plot(df["Date"], df["Close"])
    plt.title(f"{coin} Closing Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Normalized Close Price")
    plt.grid(True)
    plt.show()
