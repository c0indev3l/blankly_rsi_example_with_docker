import os
import sys
import blankly
from munch import Munch

from bot_core import init, price_event


def main():
    print("Run live with :")
    print(f"CLI args {sys.argv[1:]}")
    params = os.getenv("PARAMS", default=None)
    print(f"PARAMS ENV VAR '{params}'")

    # Authenticate Binance strategy
    exchange = blankly.Binance()

    # Use our strategy helper on Binance
    strategy = blankly.Strategy(exchange)

    # Run the price event function every time we check for a new price - by default that is 15 seconds
    variables = {"BTC-USDT": Munch()}
    strategy.add_price_event(
        price_event, symbol="BTC-USDT", resolution="1d", init=init, variables=variables
    )

    strategy.start()


if __name__ == "__main__":
    main()
