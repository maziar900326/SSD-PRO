import MetaTrader5 as mt5
import pandas as pd


class MT5Loader:

    def __init__(self):
        if not mt5.initialize():
            raise Exception("MT5 initialization failed")

    def load(self, symbol="XAUUSD", timeframe=mt5.TIMEFRAME_M15, bars=500):

        rates = mt5.copy_rates_from_pos(
            symbol,
            timeframe,
            0,
            bars
        )

        df = pd.DataFrame(rates)
        df["time"] = pd.to_datetime(df["time"], unit="s")

        return df

    def shutdown(self):
        mt5.shutdown()