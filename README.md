# Blankly example to run inside Docker containers

## Run a backtest
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

# Run a paper trade
### Docker-compose commands
```
$ cd docker/papertrade
$ docker compose up
(with eventualy --build)
```
