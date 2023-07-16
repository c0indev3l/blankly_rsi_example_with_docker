def main():
    print(f"Run backtest with {sys.argv[1:]}")

    # Define exchange as KeylessExchange
    exchange = blankly.KeylessExchange(
        price_reader=blankly.data.data_reader.PriceReader("./data/XBTUSDT_1D.csv", "BTC-USD")
    )

    # Use our strategy helper on Binance
    strategy = blankly.Strategy(exchange)

    # Run the price event function every time we check for a new price - by default that is 15 seconds
    strategy.add_price_event(price_event, symbol='BTC-USD', resolution='1d', init=init)

    #strategy.start()
    results = strategy.backtest(to='1y', initial_values={'USD': 10000})
    print(results)

if __name__ == "__main__":
    main()