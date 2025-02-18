from utils import load_data, get_external_data, analyze_price_trends
import pandas as pd
import os


csv_path = "data/products.csv"
API_URL = "https://fakestoreapi.com/products"


def generate_report(data):
    insights = data[['product_name', 'our_price', 'avg_market_price', 'price_difference', 'pricing_trend']]
    with open("report.md", "w", encoding="utf-8") as file:
        file.write("# Product Pricing Insights\n\n")
        file.write("This report provides insights into the product pricing trends.\n\n")
        file.write(insights.to_markdown(index=False))

if __name__ == "__main__":
    products = load_data(csv_path)
    external_data = get_external_data(API_URL)
    if products is not None and external_data is not None:
        if "our_price" not in products.columns:
            raise KeyError("Error: The column 'our_price' is not in the CSV file. Please check.")
        comparison = analyze_price_trends(products, external_data)

        market_prices = pd.DataFrame(external_data)["price"]
        avg_market_price = market_prices.mean()
        print(f"Average price in Fake Store API: {avg_market_price:.2f}")

        generate_report(comparison)
    else:
        print("Error loading data.")