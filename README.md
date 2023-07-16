# Blankly example to run inside Docker containers

## Run a backtest
### Run locally (ie without Docker)
```
$ python runner.py backtest
```

### Docker commands
```
$ docker build . -t backtest -f Dockerfile.backtest
$ docker run backtest
```

### Docker-compose commands
```
$ cd docker/backtest
$ docker compose up
(with eventualy --build)
```

## Run a paper trade
### Run locally (ie without Docker)
```
$ python runner.py papertrade
```

### Docker-compose commands
```
$ cd docker/papertrade
$ docker compose up
(with eventualy --build)
```

## Run a live trade session
### Run locally (ie without Docker)
```
$ python runner.py live
```

### Docker-compose commands
```
$ cd docker/live
$ docker compose up
(with eventualy --build)
```
