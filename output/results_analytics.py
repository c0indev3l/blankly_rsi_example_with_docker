import json
import pandas as pd
from bokeh.plotting import show


def load_backtests(query, db_uri):
    df = pd.read_sql(query, db_uri)
    for col in ["scheduled_time", "start_time", "end_time"]:
        df[col] = pd.to_datetime(df[col])
    
    # parse input JSON and normalize
    df["input"] = df["input"].map(lambda s: json.loads(s))
    df_input = pd.json_normalize(df["input"])

    # parse output JSON and normalize
    df["output"] = df["output"].map(lambda s: json.loads(s))
    df_output = pd.json_normalize(df["output"])
    metrics = [
        "calmar",
        "cagr",
        "cavr",
        "cum_returns",
        "max_drawdown",
        "resampled_time",
        "risk_free_rate",
        "sharpe",
        "sortino",
        "value_at_risk",
        "variance",
        "volatility",
    ]
    for metric in metrics:
        for col in [f"metrics.{metric}.display_name", f"metrics.{metric}.type"]:
            assert col in df_output.columns, f"column {col} not in df columns"
            del df_output[col]
    df_output = df_output.rename(
        columns={"start_time": "trade_start_time", "stop_time": "trade_stop_time"}
    )
    for col in ["trade_start_time", "trade_stop_time"]:
        df_output[col] = pd.to_datetime(df_output[col], unit="s")
    del df["output"]

    # concatenate input params, output metrics with others columns
    df = pd.concat([df, df_input, df_output], axis=1)
    df.set_index("id", inplace=True)
    return df


def get_history(df, id):
    df_hist = df.loc[id, "history"]
    df_hist = pd.DataFrame.from_records(df_hist)
    df_hist["time"] = pd.to_datetime(df_hist["time"], unit="s")
    df_hist.set_index("time", inplace=True)
    df_hist.plot()
    return df_hist


def main():
    pd.options.display.max_columns = 30
    query = "SELECT * FROM backtest_runs"
    db_uri = "sqlite:///backtests.sqlite"
    df = load_backtests(query, db_uri)
    print(df)
    print(df.dtypes)
    df.to_excel("backtests.xlsx")


if __name__ == "__main__":
    main()
