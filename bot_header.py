import sys
import pathlib
import blankly


def price_event(price, symbol, state: blankly.StrategyState):
    """ This function will give an updated price every 15 seconds from our definition below """
    state.variables.history.append(price)

    rsi = blankly.indicators.rsi(state.variables.history)
    current_position = state.interface.account[state.base_asset].available

    if rsi[-1] < 30 and not current_position:
        # Dollar cost average buy
        buy = blankly.trunc(state.interface.cash / price, state.variables.precision)
        state.interface.market_order(symbol, side='buy', size=buy)

    elif rsi[-1] > 70 and current_position:
        # Sell our position
        state.interface.market_order(symbol, side='sell', size=current_position)


def init(symbol, state: blankly.StrategyState):
    # Download price data to give context to the algo
    state.variables.history = state.interface.history(symbol, to=150, return_as='deque',
                                                      resolution=state.resolution)['close']

    # Get the max precision for this symbol from the API
    #increment = next(product['base_increment']
    #                 # for product in state.interface.get_products()
    #                 for product in state.interface.get_order_filter('symbol')
    #                 if product['symbol'] == symbol)
    #state.variables.precision = blankly.utils.increment_to_precision(increment)
    state.variables.precision = 2
