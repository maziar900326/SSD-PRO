import unittest
from datetime import datetime

from src.models.candle import Candle
from src.models.swing import Swing
from src.models.structure import Structure

from src.core.builders.bullish_bos_builder import BullishBOSBuilder


class TestBullishBOSBuilder(unittest.TestCase):

    def test_empty_structure_returns_no_bos(self):

        builder = BullishBOSBuilder([], [])

        result = builder.build()

        self.assertEqual(result, [])

    def test_single_bullish_bos(self):

        candles = [

            Candle(
                datetime.now(),
                10,
                12,
                9,
                11,
                100
            ),

            Candle(
                datetime.now(),
                11,
                13,
                10,
                12,
                100
            ),

            Candle(
                datetime.now(),
                12,
                14,
                11,
                13,
                100
            ),

            Candle(
                datetime.now(),
                13,
                14,
                12,
                13,
                100
            ),

            Candle(
                datetime.now(),
                13,
                16,
                12,
                15,
                100
            ),
        ]

        swing = Swing(
            index=2,
            time=candles[2].time,
            price=14,
            swing_type=Swing.HIGH
        )

        structure = Structure(
            Structure.HH,
            swing
        )

        builder = BullishBOSBuilder(
            candles,
            [structure]
        )

        result = builder.build()

        self.assertEqual(len(result), 1)

        self.assertTrue(result[0].is_bullish)

        self.assertEqual(result[0].price, 14)

        self.assertEqual(result[0].candle_index, 4)


if __name__ == "__main__":
    unittest.main()