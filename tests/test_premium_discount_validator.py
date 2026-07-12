import unittest

from src.core.validators.premium_discount_validator import (
    PremiumDiscountValidator,
)


class TestPremiumDiscountValidator(unittest.TestCase):

    def setUp(self):
        self.validator = PremiumDiscountValidator()

    def test_valid_range(self):

        self.assertTrue(
            self.validator.validate(
                swing_high=1.1200,
                swing_low=1.1000,
            )
        )

    def test_missing_high(self):

        with self.assertRaises(ValueError):
            self.validator.validate(
                swing_high=None,
                swing_low=1.1000,
            )

    def test_missing_low(self):

        with self.assertRaises(ValueError):
            self.validator.validate(
                swing_high=1.1200,
                swing_low=None,
            )

    def test_invalid_range(self):

        with self.assertRaises(ValueError):
            self.validator.validate(
                swing_high=1.1000,
                swing_low=1.1200,
            )

    def test_zero_range(self):

        with self.assertRaises(ValueError):
            self.validator.validate(
                swing_high=1.1000,
                swing_low=1.1000,
            )


if __name__ == "__main__":
    unittest.main()