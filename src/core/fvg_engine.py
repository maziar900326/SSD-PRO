from src.core.builders.bullish_fvg_builder import (
    BullishFVGBuilder,
)
from src.core.builders.bearish_fvg_builder import (
    BearishFVGBuilder,
)


class FVGEngine:

    def __init__(self, candles):

        self.candles = candles

        self.bullish_builder = BullishFVGBuilder()

        self.bearish_builder = BearishFVGBuilder()

    def find_bullish(self):

        return self.bullish_builder.build(
            self.candles
        )

    def find_bearish(self):

        return self.bearish_builder.build(
            self.candles
        )

    def find_all(self):

        bullish = self.find_bullish()

        bearish = self.find_bearish()

        return bullish + bearish