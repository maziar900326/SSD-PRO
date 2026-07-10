class ImpulseDetector:
    """
    Detects strong impulsive candles.

    Version 0.5.0

    Future versions may include:

    - ATR
    - Volume
    - Multi Candle Impulse
    - Body Percentage
    """

    def is_bullish_impulse(
        self,
        base,
        impulse
    ):

        if not impulse.bullish:
            return False

        if impulse.body <= base.body:
            return False

        return True

    def is_bearish_impulse(
        self,
        base,
        impulse
    ):

        if not impulse.bearish:
            return False

        if impulse.body <= base.body:
            return False

        return True