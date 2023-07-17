import os
import sys
import datetime

import blankly
import sqlalchemy
from sqlalchemy.orm import Session

from db import BacktestRun, Base
import json
from munch import Munch

import numpy as np

from bot_core import init, price_event
from parameter_explorer import ParameterExplorer


def main():
    scheduled_time = datetime.datetime.now()
    uri = "sqlite:///output/backtests.sqlite"
    engine = sqlalchemy.create_engine(uri)
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
    """
    # One point exploration
    explorer.add_parameter("rsi_period", 14)
    explorer.add_parameter("rsi_min", 30.0)
    explorer.add_parameter("rsi_max", 70.0)
    """
    explorer.add_parameter("rsi_period", 14, np.arange(start=10, stop=20, step=1), int)
    explorer.add_parameter(
        "rsi_min", 30.0, np.linspace(start=0, stop=100, num=11), float
    )
    explorer.add_parameter(
        "rsi_max", 70.0, np.linspace(start=0, stop=100, num=11), float
    )
    # explorer.add_parameter("dir", "BUY", ["BUY", "SELL"], str)
    explorer.add_constraint(lambda p: p.rsi_min < p.rsi_max)

    count = explorer.count_runs
    for i, parameter in enumerate(explorer.parameters(), start=1):
        # Use our strategy helper on Binance
        strategy = blankly.Strategy(exchange)

        # Run the price event function every time we check for a new price - by default that is 15 seconds
        d_param = parameter._asdict()
        variables = {
            "BTC-USD": Munch(**d_param),
        }
        strategy.add_price_event(
            price_event,
            symbol="BTC-USD",
            resolution="1d",
            init=init,
            variables=variables,
        )

        print(f"Run backtest {i} / {count} with {variables}")
        # strategy.start()  # papertrade / live
        results = strategy.backtest(to="3y", initial_values={"USD": 10000})
        end_time = datetime.datetime.now()
        print(results)

        json_params = json.dumps(d_param)

        d_results = results.to_dict()
        json_results = json.dumps(d_results)
        # with open("output/results.json", "w") as fd:
        #    json.dump(d_results, fd)

        run = BacktestRun(
            scheduled_time=scheduled_time,
            start_time=scheduled_time,
            end_time=end_time,
            input=json_params,
            output=json_results,
        )
        print("Commit to database")
        with Session(engine) as session:
            session.add(run)
            session.commit()


if __name__ == "__main__":
    main()
