import numpy as np
from parameter_explorer import ParamaterExplorer, to_param_string


def main():
    explorer = ParamaterExplorer()
    explorer.add_parameter("rsi_period", 14, np.arange(start=10, stop=20, step=1), int)
    explorer.add_parameter("rsi_min", 30.0, np.linspace(start=0, stop=100, num=11), float)
    explorer.add_parameter("rsi_max", 70.0, np.linspace(start=0, stop=100, num=11), float)
    # explorer.add_parameter("dir", "BUY", ["BUY", "SELL"], str)
    explorer.add_constraint(lambda p: p.rsi_min < p.rsi_max)

    print(explorer)
    print()
    count = explorer.count_runs
    print(f"\tCount: {count}")
    print()
    print(f"\tDefault: {explorer.default_parameter}")
    print(f"\t\t{to_param_string(explorer.default_parameter)}")
    print()
    for i, param in enumerate(explorer.parameters()):
        print(i, param)
        # print("\t", to_param_string(param))

if __name__ == "__main__":
    main()
