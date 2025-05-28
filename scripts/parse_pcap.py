import pandas as pd
import numpy as np
import time

#mock version no real data
def generate_mock_data(num_rows=10000):
    now = time.time()
    timestamps = [now + i * 0.1 for i in range(num_rows)]
    prices = 100 + np.cumsum(np.random.randn(num_rows) * 0.05)
    sizes = np.random.randint(10, 500, size=num_rows)

    df = pd.DataFrame({
        "timestamp": timestamps,
        "symbol": ["AAPL"] * num_rows,
        "price": prices,
        "size": sizes,
        "type": ["order"] * num_rows
    })

    df.to_csv("data/raw_orders.csv", index=False)
    print("✅ Mock data generated.")
    return df

if __name__ == "__main__":
    generate_mock_data()
