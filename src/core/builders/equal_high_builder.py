from src.models.liquidity import Liquidity
from src.models.swing import Swing


class EqualHighBuilder:
    """
    Detects Equal High liquidity zones.
    """

    DEFAULT_TOLERANCE = 0.0005

    def __init__(self, swings, tolerance=None):
        self.swings = swings
        self.tolerance = (
            tolerance
            if tolerance is not None
            else self.DEFAULT_TOLERANCE
        )

    def build(self):
        """
        Builds all Equal High liquidity zones.
        """

        highs = self._get_high_swings()

        liquidity = self._find_equal_highs(highs)

        return liquidity

    def _get_high_swings(self):

        result = []

        for swing in self.swings:

            if swing.is_high:
                result.append(swing)

        return result

    def _find_equal_highs(self, highs):

        zones = []

        for i in range(len(highs) - 1):

            first = highs[i]

            second = highs[i + 1]

            difference = abs(
                first.price - second.price
            )

            if difference <= self.tolerance:

                upper = max(
                    first.price,
                    second.price
                )

                lower = min(
                    first.price,
                    second.price
                )

                zones.append(

                    Liquidity(

                        liquidity_type=Liquidity.EQH,

                        first_swing=first,

                        second_swing=second,

                        upper_price=upper,

                        lower_price=lower

                    )

                )

        return zones