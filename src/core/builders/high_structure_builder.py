from src.models.structure import Structure


class HighStructureBuilder:

    def __init__(self, highs):
        self.highs = highs

    def build(self):

        structures = []

        if len(self.highs) < 2:
            return structures

        previous = self.highs[0]

        for current in self.highs[1:]:

            if current.price > previous.price:

                structures.append(
                    Structure(
                        Structure.HH,
                        current
                    )
                )

            else:

                structures.append(
                    Structure(
                        Structure.LH,
                        current
                    )
                )

            previous = current

        return structures