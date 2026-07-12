class PremiumDiscountValidator:

    def validate(
        self,
        swing_high,
        swing_low,
    ):
        """
        Validate Premium / Discount inputs.

        Parameters
        ----------
        swing_high : float

        swing_low : float

        Returns
        -------
        bool

        Raises
        ------
        ValueError
        """

        if swing_high is None:
            raise ValueError(
                "Swing High is required."
            )

        if swing_low is None:
            raise ValueError(
                "Swing Low is required."
            )

        if swing_high <= swing_low:
            raise ValueError(
                "Swing High must be greater than Swing Low."
            )

        if (swing_high - swing_low) <= 0:
            raise ValueError(
                "Trading range must be greater than zero."
            )

        return True