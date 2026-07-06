from src.models.trend import Trend


class TrendEngine:

    def __init__(self, swings):
        self.swings = swings

    def run(self):

        # برای تشخیص روند حداقل به 4 Swing نیاز داریم
        if len(self.swings) < 4:
            return Trend(Trend.RANGE)

        highs = self._get_highs()
        lows = self._get_lows()

        if self._is_uptrend(highs, lows):
            return Trend(
                Trend.UPTREND,
                self.swings[0].index,
                self.swings[-1].index
            )

        if self._is_downtrend(highs, lows):
            return Trend(
                Trend.DOWNTREND,
                self.swings[0].index,
                self.swings[-1].index
            )

        return Trend(
            Trend.RANGE,
            self.swings[0].index,
            self.swings[-1].index
        )

    def _get_highs(self):
        return [
            swing
            for swing in self.swings
            if swing.is_high
        ]

    def _get_lows(self):
        return [
            swing
            for swing in self.swings
            if swing.is_low
        ]

    def _is_uptrend(self, highs, lows):

        if len(highs) < 2 or len(lows) < 2:
            return False

        return (
            highs[-1].price > highs[-2].price and
            lows[-1].price > lows[-2].price
        )

    def _is_downtrend(self, highs, lows):

        if len(highs) < 2 or len(lows) < 2:
            return False

        return (
            highs[-1].price < highs[-2].price and
            lows[-1].price < lows[-2].price
        )