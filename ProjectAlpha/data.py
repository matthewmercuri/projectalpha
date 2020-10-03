from tngo import Tiingo

Tiingo = Tiingo()


class Data:
    def __init__(self, source):
        self.source = source

    def price(self, symbol):
        if self.source == "tiingo":
            price = Tiingo.price(symbol)

        return price

    def daily_data(self, symbol, full=True, start_date=None,
                   end_date=None, save_locally=False):
        if self.source == "tiingo":
            dd = Tiingo.daily_data(symbol, full, start_date, end_date,
                                   save_locally)

        return dd

    def valid_symbols(self):
        if self.source == "tiingo":
            valid_syms = Tiingo.valid_symbols()

        return valid_syms

    def is_valid(self, symbol):
        if self.source == "tiingo":
            valid = Tiingo.is_valid(symbol)

        if valid is False:
            raise NameError('Symbol is not found')

    def symbol_meta(self, symbol):
        if self.source == "tiingo":
            meta = Tiingo.symbol_meta(symbol)

        return meta
