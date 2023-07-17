import os
import sys
import datetime

import blankly
import sqlalchemy
from sqlalchemy.orm import Session

from db import BacktestRun, Base
import json
from munch import Munch

from bot_core import init, price_event
from parameter_explorer import ParameterExplorer


def main():
    scheduled_time = datetime.datetime.now()
    engine = sqlalchemy.create_engine("sqlite:///output/backtests.sqlite")
    # conn = engine.connect()
    Base.metadata.create_all(engine)

    print("Run backtest with :")
    print(f"CLI args {sys.argv[1:]}")
    params = os.getenv("PARAMS", default=None)
    print(f"PARAMS ENV VAR '{params}'")

    # Define exchange as KeylessExchange
    exchange = blankly.KeylessExchange(
        price_reader=blankly.data.data_reader.PriceReader(
            "./data/XBTUSDT_1D.csv", "BTC-USD"
        )
    )

    # define exploration, constraints
    explorer = ParameterExplorer()
    explorer.add_parameter("rsi_period", 14)
    explorer.add_parameter("rsi_min", 30.0)
    explorer.add_parameter("rsi_max", 70.0)

    for parameter in explorer.parameters():
        # Use our strategy helper on Binance
        strategy = blankly.Strategy(exchange)

        # Run the price event function every time we check for a new price - by default that is 15 seconds
        variables = {
            "BTC-USD": Munch(**parameter._asdict()),
        }
        strategy.add_price_event(
            price_event, symbol="BTC-USD", resolution="1d", init=init, variables=variables
        )

        print(f"Run backtest with {variables}")
        # strategy.start()  # papertrade / live
        results = strategy.backtest(to="3y", initial_values={"USD": 10000})
        end_time = datetime.datetime.now()
        print(results)

        d_results = results.to_dict()
        json_results = json.dumps(d_results)
        # with open("output/results.json", "w") as fd:
        #    json.dump(d_results, fd)

        run = BacktestRun(
            scheduled_time=scheduled_time,
            start_time=scheduled_time,
            end_time=end_time,
            input=params,
            output=json_results,
        )
        with Session(engine) as session:
            session.add(run)
            session.commit()


if __name__ == "__main__":
    main()
