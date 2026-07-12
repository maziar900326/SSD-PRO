import unittest

from src.core.builders.fvg_mitigation_builder import (
    FVGMitigationBuilder,
)


class DummyFVG:

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


class TestFVGMitigationBuilder(unittest.TestCase):

    def test_fvg_mitigation(self):

        fvgs = [

            DummyFVG(
                upper_price=1.1050,
                lower_price=1.1040,
                index=10,
            )

        ]

        candles = [

            DummyCandle(
                time="2026-01-02",
                high=1.1055,
                low=1.1035,
                index=20,
            )

        ]

        builder = FVGMitigationBuilder()

        mitigations = builder.build(
            candles=candles,
            fvgs=fvgs,
        )

        self.assertEqual(
            len(mitigations),
            1,
        )

        self.assertTrue(
            fvgs[0].mitigated,
        )

        self.assertEqual(
            mitigations[0].zone_type,
            "FVG",
        )

        self.assertEqual(
            mitigations[0].index,
            20,
        )


if __name__ == "__main__":
    unittest.main()