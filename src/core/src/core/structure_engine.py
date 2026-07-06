from src.models.structure import Structure


class StructureEngine:

    def __init__(self, swings):
        self.swings = swings

    def run(self):

        highs = self._extract_highs()
        lows = self._extract_lows()

        structures = []

        structures.extend(
            self._build_high_structure(highs)
        )

        structures.extend(
            self._build_low_structure(lows)
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

    def _build_high_structure(self, highs):
        return []

    def _build_low_structure(self, lows):
        return []