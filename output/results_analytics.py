import json
import pandas as pd


def main():
    pd.options.display.max_columns = 10
    df = pd.read_sql("SELECT * FROM backtest_runs", "sqlite:///backtests.sqlite")
    df.set_index("id", inplace=True)
    df["output"] = df["output"].map(lambda s: json.loads(s))
    df_output = pd.json_normalize(df["output"])
    df = pd.concat([df, df_output], axis=1)
    print(df)
    print(df.dtypes)
    df.to_excel("backtests.xlsx")


if __name__ == "__main__":
    main()
