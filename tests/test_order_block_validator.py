import unittest
from datetime import datetime

from src.core.validators.order_block_validator import (
    OrderBlockValidator,
)
from src.models.candle import Candle
from src.models.order_block import OrderBlock


class TestOrderBlockValidator(unittest.TestCase):

    def test_valid_order_block(self):

        base = Candle(
            time=datetime.now(),
            open=100,
            high=105,
            low=95,
            close=96,
            volume=1000
        )

        impulse = Candle(
            time=datetime.now(),
            open=96,
            high=112,
            low=95,
            close=111,
            volume=2500
        )

        block = OrderBlock(
            block_type=OrderBlock.BULLISH,
            base_candle=base,
            impulse_candle=impulse,
            upper_price=105,
            lower_price=95
        )

        validator = OrderBlockValidator()

        self.assertTrue(
            validator.validate(block)
        )

    def test_invalid_order_block(self):

        base = Candle(
            time=datetime.now(),
            open=100,
            high=105,
            low=95,
            close=96,
            volume=1000
        )

        impulse = Candle(
            time=datetime.now(),
            open=96,
            high=112,
            low=95,
            close=111,
            volume=2500
        )

        block = OrderBlock(
            block_type=OrderBlock.BULLISH,
            base_candle=base,
            impulse_candle=impulse,
            upper_price=105,
            lower_price=95,
            is_valid=False
        )

        validator = OrderBlockValidator()

        self.assertFalse(
            validator.validate(block)
        )


if __name__ == "__main__":
    unittest.main()