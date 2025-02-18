# MarketMatch - Price Analysis for Small Business

## Description
Market is a price analysis tool that allows small businesses to compare their prices with market trends. It uses internal data from a CSV file and contrasts tt with data obtained from the "Fake Store API" (but it can be changed to read any other source), providing key insights for decision-making.

## Installation and Setup
###Requirements
* Python 3.x
* Pip for dependency management

## Installing Dependencies
Before running the program, install the necessary dependencies:
```
pip install -r requirements.txt
```

## Project Structure
```
MarketMatch/
├─ data/
│   └─ products.csv # Internal product price data
├─ src/
│   └─ analysis.py  # Main analysis script
├─ requirements.txt # Project dependencies
├─ README.md        # Project documentation
└─ report.md        # Generated report after execution
```

## Execution
To run the analysis, execute the following command in the terminal:
```
python src/analysis.py
```

## Approach Explanation
1. **Load CSV data:** Internal data is processed using Pandas.
2. **Fetch external data:** Prices are retrieved from the Fake Store API (or other external source).
3. **Analyze trends:** The average market price is calculated and compared with internal prices.
4. **Generate insights:** It determines whether the products are more expensive or cheaper compared to the market.
5. **Create a Markdown report:** a ```report.md``` file is generated with the analysis results.

## Additional Notes
* If the Fake Store API is unavailable, the program will handle the error and indicate it in the console.
* Results may vary depending on the current data from the API.

## Estimated Development Time
* **Data loading and processing:** 15 minutes
* **External API integration:** 20 minutes
* **Analysis and insight generation** 25 minutes
* **Repository structure and documentation:** 20 minutes
* **TOTAL:** ~1 hour 20 minutes

© 2025 - MarketMatch