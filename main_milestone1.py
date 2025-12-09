# ----------------------------------------------------------
# MAIN MILESTONE-1 (FOR 5 COINS)
# ----------------------------------------------------------

from data_collection import download_all_coins
from data_preprocessing import preprocess_all
from dataset_creator import create_all_datasets
from plot_data import plot_close_price

def milestone1_multi():

    print("\n🚀 STARTING MILESTONE 1 FOR 5 COINS")

    # Step 1 — Download
    all_data = download_all_coins()

    # Step 2 — Preprocess
    preprocessed, scalers = preprocess_all(all_data)

    # Step 3 — Create Datasets
    datasets = create_all_datasets(preprocessed)

    # Step 4 — Optional: Plot first coin
    first_coin = list(preprocessed.keys())[0]
    plot_close_price(preprocessed[first_coin], first_coin)

    print("\n🎉 MILESTONE 1 COMPLETED FOR ALL 5 COINS!")

    return all_data, preprocessed, datasets, scalers


if __name__ == "__main__":
    milestone1_multi()
