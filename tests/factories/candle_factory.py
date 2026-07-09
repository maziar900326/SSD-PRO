from datetime import datetime

from src.models.candle import Candle


def make_candle(
    time=None,
    open=100.0,
    high=105.0,
    low=95.0,
    close=102.0,
    volume=100
):
    """
    Creates a Candle object for tests.

    Any field can be overridden.
    """

    return Candle(
        time=time or datetime.now(),
        open=open,
        high=high,
        low=low,
        close=close,
        volume=volume
    )


def make_bullish_candle(**kwargs):
    """
    Creates a bullish candle.
    """

    defaults = dict(
        open=100,
        high=106,
        low=99,
        close=105,
        volume=100
    )

    defaults.update(kwargs)

    return make_candle(**defaults)


def make_bearish_candle(**kwargs):
    """
    Creates a bearish candle.
    """

    defaults = dict(
        open=105,
        high=106,
        low=99,
        close=100,
        volume=100
    )

    defaults.update(kwargs)

    return make_candle(**defaults)