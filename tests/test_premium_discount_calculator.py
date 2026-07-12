import unittest

from src.core.calculators.premium_discount_calculator import (
    PremiumDiscountCalculator,
)


class TestPremiumDiscountCalculator(unittest.TestCase):

    def test_premium_zone(self):

        calculator = PremiumDiscountCalculator()

        result = calculator.calculate(
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

    def test_discount_zone(self):

        calculator = PremiumDiscountCalculator()

        result = calculator.calculate(
            swing_high=1.1200,
            swing_low=1.1000,
            current_price=1.1050,
        )

        self.assertEqual(
            result.zone,
            "DISCOUNT",
        )

    def test_equilibrium_zone(self):

        calculator = PremiumDiscountCalculator()

        result = calculator.calculate(
            swing_high=1.1200,
            swing_low=1.1000,
            current_price=1.1100,
        )

        self.assertEqual(
            result.zone,
            "EQUILIBRIUM",
        )


if __name__ == "__main__":
    unittest.main()