from tngo import Tiingo

Tiingo = Tiingo()

''' Ideally we would want this class to function completely
independantly. That way, we can use it for other projects to gather
data.
'''


class Data:
    def __init__(self, source="tiingo"):
        self.source = source

    def price(self, symbol):
        if self.source == "tiingo":
            symbol = self.symbol_check(symbol)
            price = Tiingo.price(symbol)

        return price

    def daily_data(self, symbol, full=True, start_date=None,
                   end_date=None, save_locally=False):
        if self.source == "tiingo":
            symbol = self.symbol_check(symbol)
            dd = Tiingo.daily_data(symbol, full, start_date, end_date,
                                   save_locally)

        return dd

    def symbol_meta(self, symbol):
        if self.source == "tiingo":
            symbol = self.symbol_check(symbol)
            meta = Tiingo.symbol_meta(symbol)

        return meta

    def is_valid(self, symbol):
        if self.source == "tiingo":
            valid = Tiingo.is_valid(symbol)

        if valid is False:
            raise NameError('Symbol is not found')

    def symbol_check(self, symbol):
        symbol = symbol.upper()
        self.is_valid(symbol)

        return symbol

    def valid_symbols(self):
        if self.source == "tiingo":
            valid_syms = Tiingo.valid_symbols()

        return valid_syms
