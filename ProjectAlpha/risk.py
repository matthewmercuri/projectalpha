''' Ideally, we would want to put these metrics in a df
or database with the return series of the portfolio. How
would this translate to when we use these metrics to backtest
a portfolio that trades?

- start with simpler methods like alpha, beta, etc.
- we want to start this class by being applied to the return
df (which would be the return series of the port)
- finally, we want a method that prints out ALL of the metrics
'''


class Risk:
    def __init__(self):
        pass

    def sharpe_ratio(self):
        pass

    def treynor_measure(self):
        pass

    def sortino(self):
        pass

    def max_drawdown(self):
        pass

    def var(self):
        pass

    def cvar(self):
        pass

    def cagr(self):
        pass

    def roi(self):
        pass

    def pandl(self):
        pass

    def alpha(self):
        pass

    def beta(self):
        pass

    def std(self):
        pass

    def r_squared(self):
        pass

    def corr_matrix(self):
        pass
