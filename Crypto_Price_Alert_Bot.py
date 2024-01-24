import requests
import time


def get_ethereum_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data['ethereum']['usd']

def main():
    threshold_price = 2000  # Set your desired threshold price for Ethereum here
    check_interval = 60  # Check every 60 seconds

    while True:
        try:
            current_price = get_ethereum_price()
            print(f"Current Ethereum Price: ${current_price}")
            if current_price >= threshold_price:
                print("🚀 Ethereum has entered the race! 💸")
            time.sleep(check_interval)
        except requests.RequestException as e:
            print("Error fetching price data:", e)
            time.sleep(check_interval)

if __name__ == "__main__":
    main()
