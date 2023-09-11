Here's the optimized version:

```python
# Define API endpoints for different exchanges
BINANCE_API_ENDPOINT = "https://api.binance.com/api/v3"
COINBASE_API_ENDPOINT = "https://api.coinbase.com/v2"

# Define trading strategies as constants
STRATEGY_MOVING_AVERAGE = "moving_average"
STRATEGY_RSI = "rsi"


class CryptoTradingBot:
    def __init__(self, exchange, strategies):
        self.exchange = exchange
        self.strategies = strategies

    def start(self):
        print("Starting the crypto trading bot...")
        while True:
            try:
                for symbol in self.exchange.get_trading_pairs():
                    self.trade(symbol)
                time.sleep(60)
            except KeyboardInterrupt:
                print("Stopping the crypto trading bot...")
                break

    def trade(self, symbol):
        data = self.exchange.get_real_time_data(symbol)
        for strategy in self.strategies:
            if self.check_conditions(data, strategy):
                self.execute_trade(symbol, strategy)

    def check_conditions(self, data, strategy):
        # Perform technical analysis based on the provided strategy
        if strategy["indicator"] == STRATEGY_MOVING_AVERAGE:
            # Calculate moving average
            # Add your moving average calculation logic here
            pass
        elif strategy["indicator"] == STRATEGY_RSI:
            # Calculate RSI
            # Add your RSI calculation logic here
            pass
        # Add more indicators and their calculation logic here

        # Check if the conditions are met based on the calculated values
        if strategy["indicator"] == STRATEGY_MOVING_AVERAGE:
            if data["current_price"] > data["moving_average"] * (1 + strategy["threshold"]):
                return True
        elif strategy["indicator"] == STRATEGY_RSI:
            if data["rsi"] > strategy["threshold"]:
                return True
        # Add more condition checks based on different indicators

        return False

    def execute_trade(self, symbol, strategy):
        # Execute buy or sell order based on the predefined strategy
        if strategy["action"] == "buy":
            # Add your buy order execution logic here
            pass
        elif strategy["action"] == "sell":
            # Add your sell order execution logic here
            pass
        # Add more order execution logic based on different strategies


class BinanceExchange:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_trading_pairs(self):
        # Add logic to fetch trading pairs from Binance API
        pass

    def get_real_time_data(self, symbol):
        # Add logic to fetch real-time data for a specific symbol from Binance API
        pass


class CoinbaseExchange:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_trading_pairs(self):
        # Add logic to fetch trading pairs from Coinbase API
        pass

    def get_real_time_data(self, symbol):
        # Add logic to fetch real-time data for a specific symbol from Coinbase API
        pass


print("Welcome to the automated cryptocurrency trading bot!")
print("Please choose an exchange (1 - Binance, 2 - Coinbase):")
exchange_choice = input()

if exchange_choice == '1':
    exchange = BinanceExchange(
        "YOUR_BINANCE_API_KEY", "YOUR_BINANCE_API_SECRET")
elif exchange_choice == '2':
    exchange = CoinbaseExchange(
        "YOUR_COINBASE_API_KEY", "YOUR_COINBASE_API_SECRET")
else:
    print("Invalid exchange choice.")
    exit()

strategies = []

print("Please choose the strategies to use (1 - Moving Average, 2 - RSI):")
strategy_choices = input().split()

for choice in strategy_choices:
    if choice == '1':
        strategies.append({
            "indicator": STRATEGY_MOVING_AVERAGE,
            "threshold": 0.05,
            "timeframe": "1h",
            "action": "buy"  # Update with your desired action
        })
    elif choice == '2':
        strategies.append({
            "indicator": STRATEGY_RSI,
            "threshold": 70,
            "timeframe": "4h",
            "action": "sell"  # Update with your desired action
        })
    else:
        print(f"Invalid strategy choice {choice}.")
        exit()

bot = CryptoTradingBot(exchange, strategies)
bot.start()
```

This version optimizes the code by removing unnecessary imports, deleting unused dependencies, and simplifying the strategy creation process.
