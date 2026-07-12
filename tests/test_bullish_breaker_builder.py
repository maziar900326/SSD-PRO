import unittest

from src.models.breaker import Breaker
from src.core.builders.bullish_breaker_builder import (
    BullishBreakerBuilder,
)


class DummyOrderBlock:

    def __init__(
        self,
        direction,
        upper_price,
        lower_price,
        time,
        index,
    ):
        self.direction = direction
        self.upper_price = upper_price
        self.lower_price = lower_price
        self.time = time
        self.index = index


class DummyStructure:

    def __init__(self, time, index):
        self.time = time
        self.index = index


class TestBullishBreakerBuilder(unittest.TestCase):

    def test_single_bullish_breaker(self):

        order_blocks = [

            DummyOrderBlock(
                direction="BEARISH",
                upper_price=1.1050,
                lower_price=1.1040,
                time="2026-01-01",
                index=10,
            )

        ]

        bullish_bos = [

            DummyStructure(
                time="2026-01-02",
                index=20,
            )

        ]

        builder = BullishBreakerBuilder()

        breakers = builder.build(
            candles=[],
            order_blocks=order_blocks,
            bullish_bos=bullish_bos,
        )

        self.assertEqual(len(breakers), 1)

        breaker = breakers[0]

        self.assertEqual(
            breaker.direction,
            Breaker.BULLISH,
        )

        self.assertEqual(
            breaker.upper_price,
            1.1050,
        )

        self.assertEqual(
            breaker.lower_price,
            1.1040,
        )

        self.assertEqual(
            breaker.index,
            20,
        )

        self.assertFalse(
            breaker.mitigated,
        )


if __name__ == "__main__":
    unittest.main()