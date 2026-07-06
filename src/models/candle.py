from dataclasses import dataclass
from datetime import datetime


@dataclass
class Candle:
    time: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

    @property
    def bullish(self):
        return self.close > self.open

    @property
    def bearish(self):
        return self.close < self.open

    @property
    def body(self):
        return abs(self.close - self.open)

    @property
    def upper_wick(self):
        return self.high - max(self.open, self.close)

    @property
    def lower_wick(self):
        return min(self.open, self.close) - self.low

    @property
    def range(self):
        return self.high - self.low

    @property
    def body_percent(self):
        if self.range == 0:
            return 0
        return (self.body / self.range) * 100

    @property
    def strength(self):
        if self.body_percent >= 70:
            return "Strong"
        elif self.body_percent >= 40:
            return "Normal"
        else:
            return "Weak"

    def __str__(self):
        direction = "Bullish" if self.bullish else "Bearish"

        return (
            f"{self.time}\n"
            f"Direction : {direction}\n"
            f"Body      : {self.body:.2f}\n"
            f"Range     : {self.range:.2f}\n"
            f"Strength  : {self.strength}"
        )