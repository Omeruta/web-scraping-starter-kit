import pandas as pd

def save_to_csv(data, filename='output.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Saved to {filename}")

def save_to_json(data, filename='output.json'):
    df = pd.DataFrame(data)
    df.to_json(filename, orient='records', indent=4)
    print(f"Saved to {filename}")
