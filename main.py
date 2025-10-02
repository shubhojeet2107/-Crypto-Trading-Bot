import argparse
from bot import BasicBot

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simplified Binance Futures trading bot.")
    parser.add_argument("--api-key", required=True, help="Your Binance Testnet API key.")
    parser.add_argument("--api-secret", required=True, help="Your Binance Testnet API secret.")
    parser.add_argument("--symbol", default="BTCUSDT", help="The trading symbol (e.g., BTCUSDT).")
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True, help="The order side.")
    parser.add_argument("--qty", type=float, required=True, help="The order quantity.")
    args = parser.parse_args()

    try:
        # Initialize the bot
        bot = BasicBot(args.api_key, args.api_secret)

        # Place the order based on the side
        if args.side == "BUY":
            response = bot.buy_market(args.symbol, args.qty)
        else:
            response = bot.sell_market(args.symbol, args.qty)
        
        # Print the final response from the bot
        print("\n--- Final Response ---")
        print(response)

    except Exception as e:
        # This will catch initialization errors from the bot
        print(f"Bot failed to start. Error: {e}")