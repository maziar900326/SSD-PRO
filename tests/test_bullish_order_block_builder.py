import unittest
from datetime import datetime

from src.core.builders.bullish_order_block_builder import (
    BullishOrderBlockBuilder,
)
from src.models.candle import Candle
from src.models.order_block import OrderBlock


class TestBullishOrderBlockBuilder(unittest.TestCase):

    def test_single_bullish_order_block(self):

        candles = [

            Candle(
                time=datetime.now(),
                open=100,
                high=105,
                low=95,
                close=96,
                volume=1000
            ),

            Candle(
                time=datetime.now(),
                open=96,
                high=112,
                low=95,
                close=111,
                volume=2500
            )

        ]

        builder = BullishOrderBlockBuilder(candles)

        result = builder.build()

        self.assertEqual(len(result), 1)

        block = result[0]

        self.assertTrue(block.is_bullish)

        self.assertEqual(
            block.type,
            OrderBlock.BULLISH
        )

        self.assertEqual(
            block.upper_price,
            105
        )

        self.assertEqual(
            block.lower_price,
            95
        )

        self.assertFalse(block.mitigated)

        self.assertTrue(block.is_valid)


if __name__ == "__main__":
    unittest.main()