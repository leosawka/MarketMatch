import pandas as pd
import requests
import os

csv_path = "data/products.csv"
API_URL = "https://fakestoreapi.com/products"
def load_data(csv_path):
    return pd.read_csv(csv_path)

def get_external_data():
    response = requests.get(API_URL)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

def compare_prices(products, external_data):
    external_df = pd.DataFrame(external_data)[["title", "price"]]
    external_df.rename(columns={"title": "product_name", "price": "market_price"}, inplace=True)

    merged_df = product_data.merge(external_def, on="product_name", how="left")

    merged_df["price_difference"] = merged_df["our_price"] - merged_df["market_price"]

    return merged_df


def generate_report(data):
    insights = data[['product_name', 'our_price', 'market_price', 'price_difference']]
    with open("report.md", "w") as f:
        f.write(insights.to_markdown(index=False))

if __name__ == "__main__":
    products = load_data('data/products.csv')

    API_URL = "https://api.escuelajs.co/api/v1/products"
    api_key = os.getenv('API_KEY')
    external_data = get_external_data(API_URL, api_key)

comparison = compare_prices(products, external_data)

generate_report(comparison)