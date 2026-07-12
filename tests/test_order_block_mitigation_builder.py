import unittest

from src.core.builders.order_block_mitigation_builder import (
    OrderBlockMitigationBuilder,
)


class DummyOrderBlock:

    def __init__(
        self,
        upper_price,
        lower_price,
        index,
    ):
        self.direction = "BULLISH"
        self.upper_price = upper_price
        self.lower_price = lower_price
        self.index = index
        self.mitigated = False


class DummyCandle:

    def __init__(
        self,
        time,
        high,
        low,
        index,
    ):
        self.time = time
        self.high = high
        self.low = low
        self.index = index


class TestOrderBlockMitigationBuilder(unittest.TestCase):

    def test_order_block_mitigation(self):

        order_blocks = [

            DummyOrderBlock(
                upper_price=1.1050,
                lower_price=1.1040,
                index=10,
            )

        ]

        candles = [

            DummyCandle(
                time="2026-01-02",
                high=1.1055,
                low=1.1045,
                index=20,
            )

        ]

        builder = OrderBlockMitigationBuilder()

        mitigations = builder.build(
            candles=candles,
            order_blocks=order_blocks,
        )

        self.assertEqual(
            len(mitigations),
            1,
        )

        self.assertTrue(
            order_blocks[0].mitigated,
        )

        self.assertEqual(
            mitigations[0].zone_type,
            "ORDER_BLOCK",
        )

        self.assertEqual(
            mitigations[0].index,
            20,
        )


if __name__ == "__main__":
    unittest.main()