
# Petrol Price Tracker

This project scrapes petrol price data from the [GoodReturns](https://www.goodreturns.in/petrol-price.html) website using Python. The data is then structured and presented in a DataFrame using `pandas`.

## Features

- **Web Scraping**: Extracts petrol price information from an HTML page using the `requests` library and `BeautifulSoup`.
- **Data Parsing**: Parses the HTML structure and extracts relevant data such as city name, petrol price, price changes, and dates.
- **Data Storage**: Stores the extracted data in a structured format using `pandas`.

## Prerequisites

Make sure you have the following Python libraries installed:

- `requests`
- `pandas`
- `beautifulsoup4`

You can install them via `pip`:

```bash
pip install requests pandas beautifulsoup4
