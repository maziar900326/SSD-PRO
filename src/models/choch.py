class CHOCH:

    def __init__(self, direction, price, time):
        self.direction = direction
        self.price = price
        self.time = time

    def __str__(self):
        return f"{self.direction} CHOCH | {self.time} | {self.price}"