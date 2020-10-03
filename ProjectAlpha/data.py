from tngo import Tiingo

Tiingo = Tiingo()


class Data:
    def __init__(self, source):
        self.source = source

    def price(self, symbol):
        if self.source == "tiingo":
            price = Tiingo.price(symbol)

        return price

    def daily_data(self, symbol, start, end):
        if self.source == "tiingo":
            dd = Tiingo.daily_data(symbol, start, end)

        return dd

    def valid_symbols(self):
        if self.source == "tiingo":
            valid_syms = Tiingo.valid_symbols()

        return valid_syms

    def is_valid(self, symbol):
        if self.source == "tiingo":
            valid = Tiingo.is_valid(symbol)

        return valid
