Simplified Binance Futures Trading Bot
This project is a command-line trading bot built in Python that places market orders on the Binance Futures Testnet. It was developed to fulfill the requirements of a technical assessment for a Junior Python Developer role.

The application uses the python-binance library to interact with the Binance API, handles user input through a command-line interface, and implements robust logging and error handling.

Features
Testnet Connectivity: Connects securely to the Binance Futures Testnet.

Market Orders: Supports placing both BUY (long) and SELL (short) market orders.

Command-Line Interface: Accepts all necessary parameters (API keys, symbol, side, quantity) directly from the command line.

Robust Logging: All actions, successful API calls, and errors are logged with timestamps to a bot.log file.

Error Handling: The bot gracefully handles API errors and other exceptions without crashing, providing clear output.

Prerequisites
Before you begin, ensure you have the following installed and configured:

Python 3.8 or higher.

A registered Binance Testnet account.

An API Key and Secret Key generated from your Testnet account with "Enable Futures" permissions enabled.

Setup and Installation
Follow these steps to set up the project locally.

1. Clone the Repository

First, clone the repository to your local machine:

git clone [https://github.com/shubhojeet2107/Crypto-Trading-Bot.git](https://github.com/shubhojeet2107/Crypto-Trading-Bot.git)
cd Crypto-Trading-Bot

2. Create and Activate a Virtual Environment

It is highly recommended to use a Python virtual environment to manage dependencies.

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
.\venv\Scripts\activate

3. Install Dependencies

Install the required libraries from the requirements.txt file:

pip install -r requirements.txt

How to Run the Bot
The bot is executed from the command line, and all trading parameters are passed as arguments.

Command Structure:

python main.py --api-key <YOUR_API_KEY> --api-secret <YOUR_API_SECRET> --symbol <SYMBOL> --side <SIDE> --qty <QUANTITY>

Example Commands:

To place a BUY order for 0.001 BTCUSDT:

python main.py --api-key "your_api_key_here" --api-secret "your_secret_key_here" --symbol BTCUSDT --side BUY --qty 0.001

To place a SELL order for 0.01 ETHUSDT:

python main.py --api-key "your_api_key_here" --api-secret "your_secret_key_here" --symbol ETHUSDT --side SELL --qty 0.01

The final API response from Binance, whether successful or an error, will be printed to the console.

Logging
A detailed log of all bot activities is automatically created and appended to the bot.log file in the project's root directory. This includes successful connections, order attempts, final order details, and any errors encountered.
