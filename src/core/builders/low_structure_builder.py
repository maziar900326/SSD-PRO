from src.models.structure import Structure


class LowStructureBuilder:

    def __init__(self, lows):
        self.lows = lows

    def build(self):

        structures = []

        if len(self.lows) < 2:
            return structures

        previous = self.lows[0]

        for current in self.lows[1:]:

            if current.price > previous.price:

                structures.append(
                    Structure(
                        Structure.HL,
                        current
                    )
                )

            else:

                structures.append(
                    Structure(
                        Structure.LL,
                        current
                    )
                )

            previous = current

        return structures