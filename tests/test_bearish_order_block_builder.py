import unittest
from datetime import datetime

from src.core.builders.bearish_order_block_builder import (
    BearishOrderBlockBuilder,
)
from src.models.candle import Candle
from src.models.order_block import OrderBlock


class TestBearishOrderBlockBuilder(unittest.TestCase):

    def test_single_bearish_order_block(self):

        candles = [

            Candle(
                time=datetime.now(),
                open=100,
                high=105,
                low=99,
                close=104,
                volume=1000
            ),

            Candle(
                time=datetime.now(),
                open=104,
                high=105,
                low=90,
                close=92,
                volume=2500
            )

        ]

        builder = BearishOrderBlockBuilder(candles)

        result = builder.build()

        self.assertEqual(len(result), 1)

        block = result[0]

        self.assertTrue(block.is_bearish)

        self.assertEqual(
            block.type,
            OrderBlock.BEARISH
        )

        self.assertEqual(
            block.upper_price,
            105
        )

        self.assertEqual(
            block.lower_price,
            99
        )

        self.assertFalse(block.mitigated)

        self.assertTrue(block.is_valid)


if __name__ == "__main__":
    unittest.main()