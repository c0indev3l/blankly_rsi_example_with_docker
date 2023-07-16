def main():
    print("Run backtest with :")
    print(f"CLI args {sys.argv[1:]}")
    params = os.getenv("PARAMS", default=None)
    print(f"PARAMS ENV VAR {params}")
    if params is not None:
        params = params.split(",")
        print(params)
        def gettype(name):
            t = getattr(__builtins__, name)
            if isinstance(t, type):
                return t
            raise ValueError(name)
        for param in params:
            name_typ, value = param.split("=")
            name, typ = name_typ.split("::")
            typ = gettype(typ)
            print(name, typ, value)


    # Define exchange as KeylessExchange
    exchange = blankly.KeylessExchange(
        price_reader=blankly.data.data_reader.PriceReader(
            "./data/XBTUSDT_1D.csv", "BTC-USD"
        )
    )

    # Use our strategy helper on Binance
    strategy = blankly.Strategy(exchange)

    # Run the price event function every time we check for a new price - by default that is 15 seconds
    strategy.add_price_event(price_event, symbol="BTC-USD", resolution="1d", init=init)

    # strategy.start()
    results = strategy.backtest(to="3y", initial_values={"USD": 10000})
    print(results)


if __name__ == "__main__":
    main()
