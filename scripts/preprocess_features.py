import pandas as pd
import numpy as np

def engineer_features(input_csv, output_npy):
    df = pd.read_csv(input_csv)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    df.set_index("timestamp", inplace=True)

    df_resampled = df.resample("100ms").agg({
        "price": "last",
        "size": "sum"
    }).ffill()

    features = pd.DataFrame()
    features["price"] = df_resampled["price"]
    features["size"] = df_resampled["size"]
    features["price_return"] = df_resampled["price"].pct_change().fillna(0)
    # Add up to 17 features here...

    np.save(output_npy, features.to_numpy(dtype=np.float32))

if __name__ == "__main__":
    engineer_features("data/raw_orders.csv", "features/features_day1.npy")
