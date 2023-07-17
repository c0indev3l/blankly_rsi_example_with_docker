import sys
from pathlib import Path
import shutil


def main():
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == "backtest":
            fname = Path("bot_run_backtest.html")
            dest = Path("output")
            shutil.copy(fname, dest)
        elif mode == "papertrade":
            print(f"No post-processing for {mode}")
        elif mode == "livetrade":
            print(f"No post-processing for {mode}")
        else:
            raise NotImplementedError(f"Unsupported mode '{mode}'")


if __name__ == "__main__":
    main()
