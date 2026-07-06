from src.models.swing import Swing


class SwingEngine:

    def __init__(self, candles):
        self.candles = candles

    def find_swings(self):

        swings = []

        for i in range(2, len(self.candles) - 2):

            c = self.candles[i]

            # Swing High
            if (
                c.high > self.candles[i - 1].high and
                c.high > self.candles[i - 2].high and
                c.high > self.candles[i + 1].high and
                c.high > self.candles[i + 2].high
            ):

                swings.append(
                    Swing(
                        index=i,
                        time=c.time,
                        price=c.high,
                        swing_type=Swing.HIGH
                    )
                )

            # Swing Low
            if (
                c.low < self.candles[i - 1].low and
                c.low < self.candles[i - 2].low and
                c.low < self.candles[i + 1].low and
                c.low < self.candles[i + 2].low
            ):

                swings.append(
                    Swing(
                        index=i,
                        time=c.time,
                        price=c.low,
                        swing_type=Swing.LOW
                    )
                )

        return swings