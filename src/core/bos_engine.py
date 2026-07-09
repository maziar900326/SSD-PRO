from src.core.builders.bullish_bos_builder import BullishBOSBuilder
from src.core.builders.bearish_bos_builder import BearishBOSBuilder


class BOSEngine:
    """
    Coordinates Bullish and Bearish BOS builders.
    """

    def __init__(self, candles, structures):
        self.candles = candles
        self.structures = structures

    def build(self):
        """
        Returns all BOS objects.
        """

        bullish = BullishBOSBuilder(
            self.candles,
            self.structures
        ).build()

        bearish = BearishBOSBuilder(
            self.candles,
            self.structures
        ).build()

        bos = bullish + bearish

        bos.sort(
            key=lambda x: x.candle_index
        )

        return bos