import pip._vendor.requests as requests
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

if __name__ == "__main__":
    main()

