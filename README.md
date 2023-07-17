# Blankly example to run inside Docker containers

This is a work in progress which have never been tested live.
Don't use it until you are sure!

## Run a backtest
### Run locally (ie without Docker)
```
$ python bot_run_backtest.py
```

### Docker commands
```
$ docker build . -t backtest -f Dockerfile.backtest
$ docker run backtest
```

### Docker-compose commands
```
$ cd docker/backtest
$ docker compose up --build
```

## Run a paper trade
### Run locally (ie without Docker)
```
$ python bot_run_papertrade.py
```

### Docker-compose commands
```
$ cd docker/papertrade
$ docker compose up --build
```

## Run a live trade session
### Run locally (ie without Docker)
```
$ python bot_run_live.py
```

### Docker-compose commands
```
$ cd docker/live
$ docker compose up --build
```
