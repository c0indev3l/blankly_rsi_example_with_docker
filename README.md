# Blankly example to run inside Docker containers

## Run a backtest
### Run locally (ie without Docker)
```
$ python builder.py backtest
$ python bot.py
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
$ python builder.py papertrade
$ python bot.py
```

### Docker-compose commands
```
$ cd docker/papertrade
$ docker compose up --build
```

## Run a live trade session
### Run locally (ie without Docker)
```
$ python builder.py live
$ python bot.py
```

### Docker-compose commands
```
$ cd docker/live
$ docker compose up --build
```
