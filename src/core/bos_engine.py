from src.models.bos import BOS


class BOSEngine:

    def __init__(self, swings, trend):
        self.swings = swings
        self.trend = trend

    def run(self):

        if self._is_uptrend():
            return self._find_bullish_bos()

        if self._is_downtrend():
            return self._find_bearish_bos()

        return []

    def _is_uptrend(self):
        return self.trend.direction == "UPTREND"

    def _is_downtrend(self):
        return self.trend.direction == "DOWNTREND"

    def _find_bullish_bos(self):

        highs = self._get_last_highs()

        if len(highs) < 2:
            return []

        previous_high = highs[-2]
        current_high = highs[-1]

        if current_high.price > previous_high.price:

            bos = BOS(
                BOS.BULLISH,
                current_high
            )

            return [bos]

        return []

    def _find_bearish_bos(self):
        return []

    def _get_last_highs(self):

        highs = []

        for swing in self.swings:
            if swing.is_high:
                highs.append(swing)

        return highs

    def _get_last_lows(self):

        lows = []

        for swing in self.swings:
            if swing.is_low:
                lows.append(swing)

        return lows