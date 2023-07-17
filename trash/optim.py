import datetime
import numpy as np
import sqlalchemy
from sqlalchemy.orm import Session

from parameter_explorer import ParamaterExplorer
from db import Base, BacktestRun


def main():
    scheduled_time = datetime.datetime.now()
    engine = sqlalchemy.create_engine("sqlite:///output/backtests.sqlite")
    # conn = engine.connect()
    Base.metadata.create_all(engine)

    explorer = ParamaterExplorer()
    explorer.add_parameter("rsi_period", 14, np.arange(start=10, stop=20, step=1), int)
    explorer.add_parameter(
        "rsi_min", 30.0, np.linspace(start=0, stop=100, num=11), float
    )
    explorer.add_parameter(
        "rsi_max", 70.0, np.linspace(start=0, stop=100, num=11), float
    )
    # explorer.add_parameter("dir", "BUY", ["BUY", "SELL"], str)
    explorer.add_constraint(lambda p: p.rsi_min < p.rsi_max)
    print(explorer)
    print()
    count = explorer.count_runs
    print(f"\tCount: {count}")
    print()
    print(f"\tDefault: {explorer.default_parameter}")
    # print(f"\t\t{to_param_string(explorer.default_parameter)}")
    print()

    runs = []
    with Session(engine) as session:
        for i, param in enumerate(explorer.parameters()):
            print(i, param)
            # print("\t", to_param_string(param))
            run = BacktestRun(
                scheduled_time=scheduled_time, input=to_param_string(param)
            )
            # session.add(run)
            runs.append(run)
        session.add_all(runs)
        session.commit()


if __name__ == "__main__":
    main()
