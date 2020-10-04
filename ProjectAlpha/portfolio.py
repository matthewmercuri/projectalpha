from data import Data
import numpy as np
import pandas as pd
from risk import Risk

''' This portfolio object can change over time, so we should be
able to use the same class in a trading backtest.
'''


class Portfolio(Data, Risk):
    def __init__(self, source="tiingo"):
        super().__init__(source)
        self.portfolio = {}
        self.portfolio['positions'] = {}

    def add_position(self, symbol, shares):
        ''' May want to add other info about the position, like
        currency
        '''
        self.symbol_check(symbol)
        self.portfolio['positions'][symbol] = {"shares": shares}

    def delete_position(self, symbol, shares):
        pass

    def add_cash(self, cash, currency):
        pass

    def history(self):
        ''' Later will have to adjust to a one currency
        - after getting position values, add cash value col and total
        - perhaps this will only be used to show a non-trading portfolio
        '''
        positions = self.portfolio['positions']

        frames = []

        for position in positions:
            symbol = position
            shares = positions[position]['shares']

            symbol_df = self.daily_data(symbol)
            symbol_df = symbol_df['adjClose']
            symbol_df = symbol_df * shares
            # below line works as it is technically a series
            symbol_df = symbol_df.rename(symbol)

            frames.append(symbol_df)

        df = pd.concat(frames, axis=1, sort=False, names=['A', 'B'])
        df['Total Value'] = df.sum(axis=1)
        df['Percent Return'] = df['Total Value'].pct_change()
        df['Log Return'] = (np.log(df['Total Value'])
                            - np.log(df['Total Value'].shift(1)))

        return df

    def return_series(self):
        ''' This is what should be passed to the risk metrics
        '''
        df = self.history()
        return_series = df['Total Value']

        return return_series

    def export(self):
        pass

    def import_portfolio(self, portfolio):
        ''' First need to check if the portfolio that is passed is
        valid. Otherwise, this acutally might be this simple.
        '''
        self.portfolio = portfolio

    def chart(self):
        pass

    def add_benchmark(self, benchmark):
        pass


Portfolio = Portfolio()
Portfolio.add_position('AAPL', 10)
Portfolio.add_position('AMD', 20)
# print(Portfolio.portfolio)
# print(Portfolio.daily_data('AAPL'))
print(Portfolio.history())
# print(Portfolio.symbol_meta('AAPL'))
