from src.models.swing import Swing


class Liquidity:
    """
    Represents a liquidity zone in the market.

    Version 0.4.0 supports:

    - Equal High (EQH)
    - Equal Low (EQL)
    """

    EQH = "EQH"
    EQL = "EQL"

    def __init__(
        self,
        liquidity_type,
        first_swing,
        second_swing,
        upper_price,
        lower_price
    ):
        self.type = liquidity_type

        self.first_swing = first_swing
        self.second_swing = second_swing

        self.upper_price = upper_price
        self.lower_price = lower_price

    @property
    def is_eqh(self):
        return self.type == Liquidity.EQH

    @property
    def is_eql(self):
        return self.type == Liquidity.EQL

    @property
    def center_price(self):
        """
        Returns the center price
        of the liquidity zone.
        """
        return (self.upper_price + self.lower_price) / 2

    @property
    def width(self):
        """
        Returns the height of the
        liquidity zone.
        """
        return abs(self.upper_price - self.lower_price)

    @property
    def first_time(self):
        return self.first_swing.time

    @property
    def second_time(self):
        return self.second_swing.time

    def __str__(self):

        return (
            f"{self.type}\n"
            f"Zone : {self.lower_price} -> {self.upper_price}\n"
            f"First Swing  : {self.first_time}\n"
            f"Second Swing : {self.second_time}"
        )