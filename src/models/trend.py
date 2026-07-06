class Trend:

    UPTREND = "UPTREND"
    DOWNTREND = "DOWNTREND"
    RANGE = "RANGE"

    def __init__(self, direction, start_index=None, end_index=None):
        self.direction = direction
        self.start_index = start_index
        self.end_index = end_index

    def __str__(self):
        return (
            f"{self.direction} "
            f"({self.start_index} -> {self.end_index})"
        )