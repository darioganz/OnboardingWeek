import pip._vendor.requests as requests

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data["bitcoin"]["usd"], data["ethereum"]["usd"]

def send_alert(currency, current_price, threshold):
    print(f"Alert: {currency} Price Threshold Reached!")
    print(f"The current price of {currency} is ${current_price}. It has reached the threshold of ${threshold}.")

def main():
    bitcoin_threshold = 50000  # Set your desired Bitcoin threshold
    ethereum_threshold = 3000  # Set your desired Ethereum threshold

    bitcoin_price, ethereum_price = get_crypto_prices()

    if bitcoin_price <= bitcoin_threshold:
        send_alert("Bitcoin", bitcoin_price, bitcoin_threshold)

    if ethereum_price <= ethereum_threshold:
        send_alert("Ethereum", ethereum_price, ethereum_threshold)

if __name__ == "__main__":
    main()

