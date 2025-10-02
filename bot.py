import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

# Configure logging to write to a file and print to the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        """Initializes the bot and sets the testnet URL."""
        try:
            self.client = Client(api_key, api_secret, testnet=testnet)
            # This is CRUCIAL for connecting to the futures testnet
            if testnet:
                self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
            
            # Check server connection
            self.client.futures_ping()
            logging.info("Successfully connected to Binance Futures Testnet.")
        except BinanceAPIException as e:
            logging.error(f"Binance API Error during initialization: {e}")
            raise  # Stop the bot if it can't connect
        except BinanceRequestException as e:
            logging.error(f"Binance Request Error during initialization: {e}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred during initialization: {e}")
            raise

    def _create_market_order(self, symbol, side, qty):
        """A private helper method to create and handle market orders."""
        try:
            logging.info(f"Attempting to place a {side} order for {qty} of {symbol}...")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=Client.ORDER_TYPE_MARKET,
                quantity=qty
            )
            logging.info(f"Successfully placed {side} order: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"API Error placing {side} order for {symbol}: {e}")
            return {"error": str(e)}
        except Exception as e:
            logging.error(f"An unexpected error occurred placing {side} order: {e}")
            return {"error": str(e)}

    def buy_market(self, symbol, qty):
        """Public method to place a BUY market order."""
        return self._create_market_order(symbol, "BUY", qty)

    def sell_market(self, symbol, qty):
        """Public method to place a SELL market order."""
        return self._create_market_order(symbol, "SELL", qty)