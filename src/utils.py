import pandas as pd
import requests

def load_data(csv_path):
    try:
        return pd.read_csv(csv_path, encoding="utf-8", sep=",", quotechar='"', on_bad_lines='skip')
    except pd.errors.ParserError as e:
            print(f"Error loading data: {e}")
            return None

def get_external_data(API_URL ):
    response = requests.get(API_URL)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")


def analyze_price_trends(products, external_data):
    external_df = pd.DataFrame(external_data)[["title", "price"]]
    external_df.rename(columns={"title": "product_name", "price": "market_price"}, inplace=True)

    avg_market_price = external_df["market_price"].mean()

    products["avg_market_price"] = avg_market_price
    products["price_difference"] = products["our_price"] - avg_market_price
    products["pricing_trend"] = products["price_difference"].apply(lambda x: "Increasing" if x > 0 else "Decreasing")

    return products