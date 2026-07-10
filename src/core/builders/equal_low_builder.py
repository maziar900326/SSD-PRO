from src.models.liquidity import Liquidity
from src.models.swing import Swing


class EqualLowBuilder:
    """
    Detects Equal Low liquidity zones.
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
        Builds all Equal Low liquidity zones.
        """

        lows = self._get_low_swings()

        liquidity = self._find_equal_lows(lows)

        return liquidity

    def _get_low_swings(self):

        result = []

        for swing in self.swings:

            if swing.is_low:
                result.append(swing)

        return result

    def _find_equal_lows(self, lows):

        zones = []

        for i in range(len(lows) - 1):

            first = lows[i]
            second = lows[i + 1]

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

                        liquidity_type=Liquidity.EQL,

                        first_swing=first,

                        second_swing=second,

                        upper_price=upper,

                        lower_price=lower

                    )

                )

        return zones