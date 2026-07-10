import unittest
from datetime import datetime

from src.core.builders.bearish_choch_builder import BearishCHOCHBuilder
from src.models.candle import Candle
from src.models.structure import Structure
from src.models.swing import Swing
from src.models.trend import Trend


class TestBearishCHOCHBuilder(unittest.TestCase):

    def test_single_bearish_choch(self):

        candles = [

            Candle(datetime.now(), 15, 16, 14, 15, 100),

            Candle(datetime.now(), 15, 17, 15, 16, 100),

            Candle(datetime.now(), 16, 18, 15, 17, 100),

            Candle(datetime.now(), 17, 18, 16, 17, 100),

            Candle(datetime.now(), 17, 17, 13, 14, 100),

        ]

        swing = Swing(
            index=2,
            time=candles[2].time,
            price=15,
            swing_type=Swing.LOW
        )

        structure = Structure(
            Structure.HL,
            swing
        )

        trend = Trend(Trend.UPTREND)

        builder = BearishCHOCHBuilder(
            candles,
            [structure],
            trend
        )

        result = builder.build()

        self.assertEqual(len(result), 1)

        self.assertTrue(result[0].is_bearish)

        self.assertEqual(result[0].price, 15)

        self.assertEqual(result[0].candle_index, 4)


if __name__ == "__main__":
    unittest.main()