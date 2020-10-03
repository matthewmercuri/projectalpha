from data import Data
from risk import Risk


class Portfolio(Data, Risk):
    def __init__(self, source="tiingo"):
        super().__init__(source)
        self.portfolio = {}

    def add_position(self, symbol, shares):
        symbol = symbol.upper()
        price = self.price(symbol)
        self.portfolio[symbol] = {
                                  "shares": shares,
                                  "price": price,
                                  "value": shares*price
                                  }

    def delete_position(self, symbol, shares):
        pass

    def add_cash(self, cash, currency):
        pass

    def return_series(self):
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
