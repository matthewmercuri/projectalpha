from tngo import Tiingo


class Data:
    def __init__(self, source):
        self.source = source

    def price(self, symbol):
        return Tiingo.price(symbol)

    def daily_data(self, symbol, start, end):
        if self.source == "tiingo":
            dd = Tiingo.daily_data(symbol, start, end)

        return dd

    def valid_symbols(self):
        if self.source == "tiingo":
            valid_syms = Tiingo.valid_symbols()

        return valid_syms

    def is_valid(self, symbol):
        pass
