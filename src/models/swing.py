class Swing:
    """
    Represents a market swing point.
    """

    HIGH = "HIGH"
    LOW = "LOW"

    def __init__(self, index, time, price, swing_type):
        self.index = index
        self.time = time
        self.price = price
        self.type = swing_type

    @property
    def is_high(self):
        return self.type == Swing.HIGH

    @property
    def is_low(self):
        return self.type == Swing.LOW

    def __str__(self):
        return (
            f"{self.type} | "
            f"{self.time} | "
            f"{self.price}"
        )