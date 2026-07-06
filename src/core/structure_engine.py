from src.core.builders.high_structure_builder import HighStructureBuilder
from src.core.builders.low_structure_builder import LowStructureBuilder


class StructureEngine:

    def __init__(self, swings):
        self.swings = swings

    def run(self):

        highs = self._extract_highs()
        lows = self._extract_lows()

        structures = []

        structures.extend(
            HighStructureBuilder(highs).build()
        )

        structures.extend(
            LowStructureBuilder(lows).build()
        )

        structures.sort(
            key=lambda s: s.index
        )

        return structures

    def _extract_highs(self):

        highs = []

        for swing in self.swings:
            if swing.is_high:
                highs.append(swing)

        return highs

    def _extract_lows(self):

        lows = []

        for swing in self.swings:
            if swing.is_low:
                lows.append(swing)

        return lows