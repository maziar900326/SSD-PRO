from src.models.premium_discount import PremiumDiscount


class PremiumDiscountCalculator:

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

        trading_range = swing_high - swing_low

        equilibrium = swing_low + (trading_range / 2)

        if current_price > equilibrium:
            zone = "PREMIUM"

        elif current_price < equilibrium:
            zone = "DISCOUNT"

        else:
            zone = "EQUILIBRIUM"

        return PremiumDiscount(
            swing_high=swing_high,
            swing_low=swing_low,
            equilibrium=equilibrium,
            current_price=current_price,
            zone=zone,
        )