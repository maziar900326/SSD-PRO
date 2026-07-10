from src.core.builders.bullish_choch_builder import BullishCHOCHBuilder
from src.core.builders.bearish_choch_builder import BearishCHOCHBuilder


class CHOCHEngine:
    """
    Coordinates Bullish and Bearish CHOCH builders.
    """

    def __init__(self, candles, structures, trend):
        self.candles = candles
        self.structures = structures
        self.trend = trend

    def build(self):
        """
        Returns all CHOCH objects.
        """

        bullish = BullishCHOCHBuilder(
            self.candles,
            self.structures,
            self.trend
        ).build()

        bearish = BearishCHOCHBuilder(
            self.candles,
            self.structures,
            self.trend
        ).build()

        choch = bullish + bearish

        choch.sort(
            key=lambda x: x.candle_index
        )

        return choch