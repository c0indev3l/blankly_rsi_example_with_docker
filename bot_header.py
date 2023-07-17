import sys
import os
import blankly
from utils import get_variable, init_symbol_variables


def init(symbol, state: blankly.StrategyState):
    # Download price data to give context to the algo
    state.variables.history = state.interface.history(
        symbol, to=150, return_as="deque", resolution=state.resolution
    )["close"]

    # Get the max precision for this symbol from the API
    # increment = next(product['base_increment']
    #                 # for product in state.interface.get_products()
    #                 for product in state.interface.get_order_filter('symbol')
    #                 if product['symbol'] == symbol)
    # state.variables.precision = blankly.utils.increment_to_precision(increment)
    state.variables.precision = 2

    # strategy variables initialisation from environment variable
    init_symbol_variables(state.variables, symbol)
    state.variables[symbol].rsi_period = get_variable("rsi_period")  # 14
    state.variables[symbol].rsi_min = get_variable("rsi_min")  # 30.0
    state.variables[symbol].rsi_max = get_variable("rsi_max")  # 70.0

    print(f"Init with {state.variables}")


def price_event(price, symbol, state: blankly.StrategyState):
    """This function will give an updated price every 15 seconds from our definition below"""
    state.variables.history.append(price)

    # strategy variable initialisation from state.variables[symbol] dict
    rsi_period = state.variables[symbol].rsi_period
    rsi_min = state.variables[symbol].rsi_min
    rsi_max = state.variables[symbol].rsi_max

    rsi = blankly.indicators.rsi(state.variables.history, period=rsi_period)
    current_position = state.interface.account[state.base_asset].available

    if rsi[-1] < rsi_min and not current_position:
        # Dollar cost average buy
        buy = blankly.trunc(state.interface.cash / price, state.variables.precision)
        state.interface.market_order(symbol, side="buy", size=buy)

    elif rsi[-1] > rsi_max and current_position:
        # Sell our position
        state.interface.market_order(symbol, side="sell", size=current_position)
