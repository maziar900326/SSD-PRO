class PremiumDiscount:

    def __init__(
        self,
        swing_high,
        swing_low,
        equilibrium,
        current_price,
        zone,
    ):
        self.swing_high = swing_high
        self.swing_low = swing_low
        self.equilibrium = equilibrium
        self.current_price = current_price
        self.zone = zone

    @property
    def range(self):
        return self.swing_high - self.swing_low

    def __str__(self):
        return (
            f"{self.zone} | "
            f"High={self.swing_high} | "
            f"Low={self.swing_low} | "
            f"EQ={self.equilibrium} | "
            f"Price={self.current_price}"
        )