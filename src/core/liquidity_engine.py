from src.core.builders.equal_high_builder import EqualHighBuilder
from src.core.builders.equal_low_builder import EqualLowBuilder


class LiquidityEngine:
    """
    Coordinates all liquidity builders.

    Version 0.4.0

    - Equal High
    - Equal Low
    """

    def __init__(self, swings, tolerance=0.0005):
        self.swings = swings
        self.tolerance = tolerance

    def build(self):

        equal_highs = EqualHighBuilder(
            self.swings,
            self.tolerance
        ).build()

        equal_lows = EqualLowBuilder(
            self.swings,
            self.tolerance
        ).build()

        liquidity = equal_highs + equal_lows

        liquidity.sort(
            key=lambda zone: zone.first_swing.index
        )

        return liquidity