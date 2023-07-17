import json
import pandas as pd


def main():
    pd.options.display.max_columns = 10
    query = "SELECT * FROM backtest_runs"
    db_uri = "sqlite:///backtests.sqlite"
    df = pd.read_sql(query, db_uri)
    df.set_index("id", inplace=True)
    df["output"] = df["output"].map(lambda s: json.loads(s))
    df_output = pd.json_normalize(df["output"])
    df = pd.concat([df, df_output], axis=1)
    print(df)
    print(df.dtypes)
    df.to_excel("backtests.xlsx")


if __name__ == "__main__":
    main()
