from src.models.choch import CHOCH
from src.models.trend import Trend


class BullishCHOCHBuilder:
    """
    Responsible for detecting Bullish
    Change Of Character (CHOCH).
    """

    def __init__(self, candles, structures, trend):
        self.candles = candles
        self.structures = structures
        self.trend = trend

    def build(self):
        """
        Builds all bullish CHOCH objects.
        """

        if self.trend.direction != Trend.DOWNTREND:
            return []

        structures = self._get_lh_structures()

        broken = self._find_breaks(structures)

        return self._create_choch(broken)

    def _get_lh_structures(self):
        """
        Returns only LH structures.
        """

        result = []

        for structure in self.structures:

            if structure.is_lh:
                result.append(structure)

        return result

    def _find_breaks(self, structures):
        """
        Finds structures broken by candle close.
        """

        broken = []

        for structure in structures:

            for index in range(
                structure.index + 1,
                len(self.candles)
            ):

                candle = self.candles[index]

                if candle.close > structure.price:

                    broken.append(
                        (structure, index)
                    )

                    break

        return broken

    def _create_choch(self, broken_structures):
        """
        Creates CHOCH objects.
        """

        choch_list = []

        for structure, candle_index in broken_structures:

            choch = CHOCH(
                direction=CHOCH.BULLISH,
                broken_structure=structure,
                candle_index=candle_index
            )

            choch_list.append(choch)

        return choch_list