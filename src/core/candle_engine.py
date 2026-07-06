from src.models.candle import Candle


class CandleEngine:

    @staticmethod
    def build(df):

        candles = []

        for _, row in df.iterrows():

            candle = Candle(
                time=row["time"],
                open=row["open"],
                high=row["high"],
                low=row["low"],
                close=row["close"],
                volume=row["tick_volume"]
            )

            candles.append(candle)

        return candles