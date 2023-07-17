import sys
import uuid


def cat(fname):
    print("#" * 10 + f" {fname}" + "#" * 10)
    with open(fname, "r") as fd:
        print(fd.read())


def create_dotenv_file():
    run_id = uuid.uuid4().hex
    with open(".env", "w") as f:
        f.write(f"RUN_ID={run_id}\n")


def main():
    if len(sys.argv) == 2:
        mode = sys.argv[1]
        if mode == "backtest":
            create_dotenv_file()
            cat(".env")
            cat("bot_core.py")
            cat("bot_run_backtest.py")
            create_dotenv_file()
        elif mode == "papertrade":
            create_dotenv_file()
            cat(".env")
            cat("bot_core.py")
            cat("bot_run_papertrade.py")
        elif mode == "livetrade":
            create_dotenv_file()
            cat(".env")
            cat("bot_core.py")
            cat("bot_run_live.py")
        else:
            raise NotImplementedError(f"Unsupported mode '{mode}'")
    else:
        raise NotImplementedError("Incorrect number of arguments (1 required)")


if __name__ == "__main__":
    main()
