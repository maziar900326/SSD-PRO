from src.core.builders.bearish_order_block_builder import (
    BearishOrderBlockBuilder,
)
from src.core.builders.bullish_order_block_builder import (
    BullishOrderBlockBuilder,
)
from src.core.validators.order_block_validator import (
    OrderBlockValidator,
)


class OrderBlockEngine:
    """
    Order Block Engine.

    Coordinates:

    - Bullish Builder
    - Bearish Builder
    - Validator
    """

    def __init__(self, candles):

        self.candles = candles

        self.bullish_builder = BullishOrderBlockBuilder(candles)
        self.bearish_builder = BearishOrderBlockBuilder(candles)

        self.validator = OrderBlockValidator()

    def build(self):

        candidates = []

        candidates.extend(
            self.bullish_builder.build()
        )

        candidates.extend(
            self.bearish_builder.build()
        )

        result = []

        for block in candidates:

            if self.validator.validate(block):

                result.append(block)

        return result