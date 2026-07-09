class BOS:
    """
    Represents a Break Of Structure (BOS).

    A BOS is created when price closes beyond
    a valid market structure level.
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"

    def __init__(
        self,
        direction,
        broken_structure,
        candle_index=None
    ):
        self.direction = direction
        self.broken_structure = broken_structure
        self.candle_index = candle_index

    @property
    def is_bullish(self):
        return self.direction == BOS.BULLISH

    @property
    def is_bearish(self):
        return self.direction == BOS.BEARISH

    @property
    def price(self):
        return self.broken_structure.price

    @property
    def time(self):
        return self.broken_structure.time

    def __str__(self):
        return (
            f"{self.direction} BOS | "
            f"{self.time} | "
            f"{self.price}"
        )