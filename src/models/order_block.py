from src.models.candle import Candle


class OrderBlock:
    """
    Represents an institutional Order Block.

    Version 0.5.0

    Supported:
        - Bullish Order Block
        - Bearish Order Block
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"

    def __init__(
        self,
        block_type,
        base_candle,
        impulse_candle,
        upper_price,
        lower_price,
        is_valid=True,
        mitigated=False
    ):
        self.type = block_type

        self.base_candle = base_candle
        self.impulse_candle = impulse_candle

        self.upper_price = upper_price
        self.lower_price = lower_price

        self.is_valid = is_valid
        self.mitigated = mitigated

    @property
    def is_bullish(self):
        return self.type == OrderBlock.BULLISH

    @property
    def is_bearish(self):
        return self.type == OrderBlock.BEARISH

    @property
    def center_price(self):
        return (self.upper_price + self.lower_price) / 2

    @property
    def height(self):
        return abs(self.upper_price - self.lower_price)

    @property
    def created_time(self):
        return self.base_candle.time

    def invalidate(self):
        self.is_valid = False

    def mitigate(self):
        self.mitigated = True

    def __str__(self):
        status = "VALID" if self.is_valid else "INVALID"

        mitigation = (
            "MITIGATED"
            if self.mitigated
            else "UNMITIGATED"
        )

        return (
            f"{self.type} ORDER BLOCK\n"
            f"Zone : {self.lower_price} -> {self.upper_price}\n"
            f"Created : {self.created_time}\n"
            f"{status} | {mitigation}"
        )