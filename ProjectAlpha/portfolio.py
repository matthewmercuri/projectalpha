from data import Data
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
        self.portfolio['positions'][symbol] = {"shares": shares}

    def delete_position(self, symbol, shares):
        pass

    def add_cash(self, cash, currency):
        pass

    def return_series(self):
        positions = self.portfolio['positions']
        pass

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
print(Portfolio.portfolio)
# print(Portfolio.daily_data('AAPL'))
# print(Portfolio.symbol_meta('AAPL'))
