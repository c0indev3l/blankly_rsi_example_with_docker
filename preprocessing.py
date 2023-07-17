import sys


def cat(fname):
    print("#" * 10 + f" {fname}" + "#" * 10)
    with open(fname, "r") as fd:
        print(fd.read())


def main():
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == "backtest":
            cat("bot_core.py")
            cat("bot_run_backtest.py")
        elif mode == "papertrade":
            cat("bot_core.py")
            cat("bot_run_papertrade.py")
        elif mode == "livetrade":
            cat("bot_core.py")
            cat("bot_run_live.py")
        else:
            raise NotImplementedError(f"Unsupported mode '{mode}'")


if __name__ == "__main__":
    main()
