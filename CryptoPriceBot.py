import pip._vendor.requests as requests
<<<<<<< HEAD

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
=======
import time

def get_crypto_price(crypto_symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data[crypto_symbol]['usd']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        return None

def main():
    crypto_symbol = 'bitcoin'  # Change this to your desired cryptocurrency
    max_iterations = 10  # Change this to the desired number of iterations
    
    for _ in range(max_iterations):
        current_price = get_crypto_price(crypto_symbol)
        
        if current_price is not None:
            print(f"Current {crypto_symbol} price: ${current_price}")
        
        # Optional: Add a delay to avoid making too many requests in a short time
        time.sleep(2)  # Uncomment and customize if needed
>>>>>>> cda2fbda76048dd8c66b465f5e81062bc026aac2

if __name__ == "__main__":
    main()

