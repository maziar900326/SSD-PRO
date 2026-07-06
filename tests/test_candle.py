from datetime import datetime

from src.models.candle import Candle


def test_candle():

    candle = Candle(
        time=datetime.now(),
        open=100,
        high=110,
        low=95,
        close=108,
        volume=1000
    )

    print("Bullish :", candle.bullish)
    print("Bearish :", candle.bearish)
    print("Body    :", candle.body)
    print("Range   :", candle.range)
    print("Strength:", candle.strength)


if __name__ == "__main__":
    test_candle()