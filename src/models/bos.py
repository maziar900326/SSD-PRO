class BOS:

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"

    def __init__(
        self,
        direction,
        broken_swing,
        candle_index=None
    ):
        self.direction = direction
        self.broken_swing = broken_swing
        self.candle_index = candle_index

    @property
    def price(self):
        return self.broken_swing.price

    @property
    def time(self):
        return self.broken_swing.time

    def __str__(self):
        return (
            f"{self.direction} BOS | "
            f"{self.time} | "
            f"{self.price}"
        )