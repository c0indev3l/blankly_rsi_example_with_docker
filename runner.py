"""
Blankly bot runner

Run backtest
Usage: python runner.py backtest

Run papertrade
Usage: python runner.py papertrade

Run live
Usage: python runner.py live
"""

import sys
import pathlib
import subprocess


if __name__ == "__main__":
    if len(sys.argv) > 1:
        footer = sys.argv[1]
    else:
        footer = "backtest"
    files = ["bot_header.py", f"bot_footer_{footer}.py"]
    fname_out = pathlib.Path("bot.py")
    fname_out.unlink(missing_ok=True)
    bot_source = []
    for file in files:
        with open(file) as fd:
            content = fd.read()
            bot_source.append(content)
    bot_source = "\n\n".join(bot_source)
    print(bot_source)
    with open(fname_out, "w") as fd_out:
        fd_out.write(bot_source)
    subprocess.call([sys.executable, fname_out, *sys.argv[2:]])
    fname_out.unlink(missing_ok=True)
