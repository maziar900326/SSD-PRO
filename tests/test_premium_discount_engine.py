import unittest

from src.core.premium_discount_engine import (
    PremiumDiscountEngine,
)


class TestPremiumDiscountEngine(unittest.TestCase):

    def test_calculate(self):

        engine = PremiumDiscountEngine()

        result = engine.calculate(
            swing_high=1.1200,
            swing_low=1.1000,
            current_price=1.1150,
        )

        self.assertEqual(
            result.zone,
            "PREMIUM",
        )

        self.assertAlmostEqual(
            result.equilibrium,
            1.1100,
            places=4,
        )

        self.assertAlmostEqual(
            result.range,
            0.0200,
        )


if __name__ == "__main__":
    unittest.main()