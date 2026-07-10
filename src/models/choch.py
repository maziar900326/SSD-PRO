class CHOCH:

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"

    def __init__(
        self,
        direction,
        broken_structure,
        candle_index
    ):

        self.direction = direction
        self.broken_structure = broken_structure
        self.candle_index = candle_index

    @property
    def price(self):
        return self.broken_structure.price

    @property
    def time(self):
        return self.broken_structure.time

    @property
    def is_bullish(self):
        return self.direction == CHOCH.BULLISH

    @property
    def is_bearish(self):
        return self.direction == CHOCH.BEARISH

    def __str__(self):

        return (
            f"{self.direction} CHOCH | "
            f"{self.time} | "
            f"{self.price}"
        )