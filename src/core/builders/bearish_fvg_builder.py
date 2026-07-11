from src.models.fvg import FVG


class BearishFVGBuilder:

    def build(self, candles):
        """
        Detect all Bearish Fair Value Gaps.

        Bearish Condition:

            Candle1.low > Candle3.high

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

            if candle1.low > candle3.high:

                fvg = FVG(
                    direction=FVG.BEARISH,
                    upper_price=candle1.low,
                    lower_price=candle3.high,
                    time=candle3.time,
                    index=i + 2,
                )

                fvgs.append(fvg)

        return fvgs