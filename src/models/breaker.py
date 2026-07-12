class Breaker:

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"

    def __init__(
        self,
        direction,
        upper_price,
        lower_price,
        time,
        index,
        mitigated=False,
    ):
        self.direction = direction
        self.upper_price = upper_price
        self.lower_price = lower_price
        self.time = time
        self.index = index
        self.mitigated = mitigated

    @property
    def size(self):
        return self.upper_price - self.lower_price

    def __str__(self):
        return (
            f"{self.direction} BREAKER | "
            f"{self.time} | "
            f"{self.lower_price} -> {self.upper_price}"
        )