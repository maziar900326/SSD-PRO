import unittest
from datetime import datetime

from src.core.order_block_engine import OrderBlockEngine


from src.models.candle import Candle
from src.models.order_block import OrderBlock


class TestOrderBlockEngine(unittest.TestCase):

    def test_engine_returns_order_blocks(self):

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

        engine = OrderBlockEngine(candles)

        result = engine.build()

        self.assertEqual(len(result), 1)

        self.assertIsInstance(
            result[0],
            OrderBlock
        )

        self.assertTrue(
            result[0].is_bullish
        )

        self.assertTrue(
            result[0].is_valid
        )


if __name__ == "__main__":
    unittest.main()