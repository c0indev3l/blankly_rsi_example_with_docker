# Blankly example to run inside Docker containers

This is RSI trading strategies from https://github.com/blankly-finance/rsi-crypto-trading-bot

This example is simply an experiment to see how deployment with Docker containers can be done.

This is a work in progress which have never been tested live.
Don't use it until you are sure!

Define strategy in `bot_core.py`.

## Run a backtest

Define backtest parameters (`to`, ...) and strategy parameter exploration.

### Run locally (ie without Docker)
```
$ python bot_run_backtest.py
```

### Run with Docker commands
```
$ docker build . -t backtest -f Dockerfile.backtest
$ docker run backtest
```

### Run with Docker-compose commands
```
$ cd docker/backtest
$ docker compose up --build
```

## Run a paper trade
### Run locally (ie without Docker)
```
$ python bot_run_papertrade.py
```

### Run with Docker-compose commands
```
$ cd docker/papertrade
$ docker compose up --build
```

be aware that `restart: unless-stopped` have been set in `docker-compose.yml` so it will automatically restart and it's necessary to explicitly stop the container.
this seems to be safer than `always`. (which restart container even if it have been stopped!)

## See logs (with timestamp)
```
$ docker compose logs -t
```

### Stop with Docker-compose commands
```
$ docker compose stop
```

to stop paper trading

## Run a live trade session
### Run locally (ie without Docker)
```
$ python bot_run_live.py
```

### Run with Docker-compose commands
```
$ cd docker/live
$ docker compose up --build
```

be aware that `restart: unless-stopped` have been set in `docker-compose.yml` so it will automatically restart and it's necessary to explicitly stop the container.
this seems to be safer than `always` (which restart container even if it have been stopped!)

### Stop with Docker-compose commands
```
$ docker compose stop
```
