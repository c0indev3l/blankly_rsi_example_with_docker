def main():
    print(f"Run with {sys.argv[1:]}")

    # Authenticate Binance strategy
    exchange = blankly.Binance()

    # Use our strategy helper on Binance
    strategy = blankly.Strategy(exchange)

    # Run the price event function every time we check for a new price - by default that is 15 seconds
    strategy.add_price_event(price_event, symbol='BTC-USDT', resolution='1d', init=init)

    strategy.start()

if __name__ == "__main__":
    main()