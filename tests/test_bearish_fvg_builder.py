import unittest

from src.models.candle import Candle
from src.models.fvg import FVG
from src.core.builders.bearish_fvg_builder import (
    BearishFVGBuilder,
)


class TestBearishFVGBuilder(unittest.TestCase):

    def test_single_bearish_fvg(self):

        candles = [

            Candle(
                time="2026-01-01",
                open=1.1060,
                high=1.1070,
                low=1.1050,
                close=1.1055,
                volume=1000,
            ),

            Candle(
                time="2026-01-02",
                open=1.1050,
                high=1.1060,
                low=1.0990,
                close=1.1000,
                volume=2500,
            ),

            Candle(
                time="2026-01-03",
                open=1.0985,
                high=1.1040,
                low=1.0980,
                close=1.1035,
                volume=1800,
            ),

        ]

        builder = BearishFVGBuilder()

        fvgs = builder.build(candles)

        self.assertEqual(len(fvgs), 1)

        fvg = fvgs[0]

        self.assertEqual(
            fvg.direction,
            FVG.BEARISH,
        )

        self.assertEqual(
            fvg.upper_price,
            1.1050,
        )

        self.assertEqual(
            fvg.lower_price,
            1.1040,
        )

        self.assertEqual(
            fvg.index,
            2,
        )

        self.assertFalse(
            fvg.mitigated,
        )


if __name__ == "__main__":
    unittest.main()