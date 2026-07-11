import unittest

from src.models.candle import Candle
from src.models.fvg import FVG
from src.core.fvg_engine import FVGEngine


class TestFVGEngine(unittest.TestCase):

    def test_find_bullish_fvg(self):

        candles = [

            Candle(
                time="2026-01-01",
                open=1.0990,
                high=1.1000,
                low=1.0980,
                close=1.0995,
                volume=1000,
            ),

            Candle(
                time="2026-01-02",
                open=1.1000,
                high=1.1060,
                low=1.0990,
                close=1.1050,
                volume=2500,
            ),

            Candle(
                time="2026-01-03",
                open=1.1065,
                high=1.1080,
                low=1.1010,
                close=1.1075,
                volume=1800,
            ),

        ]

        engine = FVGEngine(candles)

        fvgs = engine.find_all()

        self.assertEqual(len(fvgs), 1)

        fvg = fvgs[0]

        self.assertEqual(fvg.direction, FVG.BULLISH)

        self.assertEqual(fvg.upper_price, 1.1010)

        self.assertEqual(fvg.lower_price, 1.1000)

        self.assertFalse(fvg.mitigated)


if __name__ == "__main__":
    unittest.main()