import sys
import requests

def main():
    # Make sure the user gave us exactly one command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Try to interpret that argument as a number of Bitcoins
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Build the request URL (swap in your actual CoinCap API key below)
    api_key = "YOUR_API_KEY_HERE"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    # Fetch the current Bitcoin price in USD
    try:
        response = requests.get(url)
        response.raise_for_status()  # catch HTTP errors
        data = response.json()
        price_usd = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Network error")
    except (KeyError, TypeError, ValueError):
        sys.exit("Unexpected API response")

    # Compute how much n Bitcoins cost right now
    cost = bitcoins * price_usd

    # Print with commas and four decimal places, e.g. $12,345.6789
    print(f"${cost:,.4f}")

if __name__ == "__main__":
    main()
