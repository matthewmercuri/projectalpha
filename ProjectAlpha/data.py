import tngo


class Data:
    def __init__(self, source):
        self.source = source

    def price(self, ticker):
        return 100

    def daily_data(self, ticker, start, end):
        if self.source == "tiingo":
            dd = tngo.daily_data(ticker, start, end)

        return dd

    def valid_symbols(self):
        if self.source == "tiingo":
            valid_syms = tngo.valid_symbols()

        return valid_syms

    def is_valid(self, ticker):
        pass
