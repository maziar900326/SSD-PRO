from src.core.calculators.premium_discount_calculator import (
    PremiumDiscountCalculator,
)
from src.core.validators.premium_discount_validator import (
    PremiumDiscountValidator,
)


class PremiumDiscountEngine:

    def __init__(self):
        self.validator = PremiumDiscountValidator()
        self.calculator = PremiumDiscountCalculator()

    def calculate(
        self,
        swing_high,
        swing_low,
        current_price,
    ):
        """
        Calculate Premium / Discount.

        Parameters
        ----------
        swing_high : float

        swing_low : float

        current_price : float

        Returns
        -------
        PremiumDiscount
        """

        self.validator.validate(
            swing_high=swing_high,
            swing_low=swing_low,
        )

        return self.calculator.calculate(
            swing_high=swing_high,
            swing_low=swing_low,
            current_price=current_price,
        )