import ccxt
import time

# Define the list of cryptocurrencies
cryptos = ["BTC", "ETH", "BNB", "XRP", "ADA", "XRP", "SOL", "DOT", "DOGE", "USDC"]

# Initialize the exchange (using Binance as an example)
exchange = ccxt.binance()

def get_price_movement(symbol):
    # Fetch the klines for the past 5 minutes
    klines = exchange.fetch_ohlcv(symbol + '/USDT', timeframe='5m', limit=2)

    # Get the opening and closing prices
    current_open = klines[1][1]  # Opening price 5 minutes ago
    current_close = klines[1][4]  # Closing price now

    return "bull" if current_close > current_open else "bear"

def print_alerts():
    print("Crypto\tMovement")
    print("------------------")
    for crypto in cryptos:
        try:
            movement = get_price_movement(crypto)
            print(f"{crypto}\t{'🟩 bull' if movement == 'bull' else '🟥 bear'}")
        except Exception as e:
            print(f"{crypto}\tError: {str(e)}")

if __name__ == "__main__":
    # Run the script every 5 minutes
    while True:
        print_alerts()
        time.sleep(300)  # 300 seconds = 5 minutes
