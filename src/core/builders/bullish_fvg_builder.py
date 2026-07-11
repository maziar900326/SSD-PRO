from src.models.fvg import FVG


class BullishFVGBuilder:

    def build(self, candles):
        """
        Detect all Bullish Fair Value Gaps.

        Bullish Condition:

            Candle1.high < Candle3.low

        Returns
        -------
        list[FVG]
        """

        fvgs = []

        if len(candles) < 3:
            return fvgs

        for i in range(len(candles) - 2):

            candle1 = candles[i]
            candle2 = candles[i + 1]
            candle3 = candles[i + 2]

            if candle1.high < candle3.low:

                fvg = FVG(
                    direction=FVG.BULLISH,
                    upper_price=candle3.low,
                    lower_price=candle1.high,
                    time=candle3.time,
                    index=i + 2,
                )

                fvgs.append(fvg)

        return fvgs