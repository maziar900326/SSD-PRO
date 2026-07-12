import unittest

from src.models.breaker import Breaker
from src.core.builders.bearish_breaker_builder import (
    BearishBreakerBuilder,
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


class TestBearishBreakerBuilder(unittest.TestCase):

    def test_single_bearish_breaker(self):

        order_blocks = [

            DummyOrderBlock(
                direction="BULLISH",
                upper_price=1.1100,
                lower_price=1.1090,
                time="2026-01-01",
                index=10,
            )

        ]

        bearish_bos = [

            DummyStructure(
                time="2026-01-02",
                index=20,
            )

        ]

        builder = BearishBreakerBuilder()

        breakers = builder.build(
            candles=[],
            order_blocks=order_blocks,
            bearish_bos=bearish_bos,
        )

        self.assertEqual(len(breakers), 1)

        breaker = breakers[0]

        self.assertEqual(
            breaker.direction,
            Breaker.BEARISH,
        )

        self.assertEqual(
            breaker.upper_price,
            1.1100,
        )

        self.assertEqual(
            breaker.lower_price,
            1.1090,
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