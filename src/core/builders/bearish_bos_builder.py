from src.models.bos import BOS


class BearishBOSBuilder:
    """
    Responsible for detecting Bearish
    Break Of Structure (BOS).
    """

    def __init__(self, candles, structures):
        self.candles = candles
        self.structures = structures

    def build(self):
        """
        Builds all bearish BOS objects.
        """

        structures = self._get_bearish_structures()

        broken = self._find_breaks(structures)

        return self._create_bos(broken)

    def _get_bearish_structures(self):
        """
        Returns only bearish structures (LL).
        """

        bearish = []

        for structure in self.structures:

            if structure.is_ll:
                bearish.append(structure)

        return bearish

    def _find_breaks(self, structures):
        """
        Finds structures whose price
        has been broken by candle close.
        """

        broken = []

        for structure in structures:

            # Search only after the structure candle.
            for index in range(
                structure.index + 1,
                len(self.candles)
            ):

                candle = self.candles[index]

                if candle.close < structure.price:

                    broken.append(
                        (structure, index)
                    )

                    break

        return broken

    def _create_bos(self, broken_structures):
        """
        Creates BOS objects.
        """

        bos_list = []

        for structure, candle_index in broken_structures:

            bos = BOS(
                direction=BOS.BEARISH,
                broken_structure=structure,
                candle_index=candle_index
            )

            bos_list.append(bos)

        return bos_list