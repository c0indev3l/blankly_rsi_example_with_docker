def main():
    print(f"Run papertrade with {sys.argv[1:]}")

    # Authenticate Binance strategy
    exchange = blankly.Binance()

    # Create a paper trade exchange:
    paper_trade = blankly.PaperTrade(exchange)

    # Use our strategy helper on Binance
    strategy = blankly.Strategy(paper_trade)

    # Run the price event function every time we check for a new price - by default that is 15 seconds
    variables = {
        "BTC-USDT": Munch()
    }
    strategy.add_price_event(price_event, symbol="BTC-USDT", resolution="1d", init=init, variables=variables)

    strategy.start()


if __name__ == "__main__":
    main()
