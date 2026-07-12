from src.models.mitigation import Mitigation


class FVGMitigationBuilder:

    def build(
        self,
        candles,
        fvgs,
    ):
        """
        Detect mitigated Fair Value Gaps.

        Parameters
        ----------
        candles : list[Candle]

        fvgs : list[FVG]

        Returns
        -------
        list[Mitigation]
        """

        mitigations = []

        for fvg in fvgs:

            if getattr(fvg, "mitigated", False):
                continue

            for candle in candles:

                if candle.index <= fvg.index:
                    continue

                fully_filled = (
                    candle.high >= fvg.upper_price
                    and
                    candle.low <= fvg.lower_price
                )

                if not fully_filled:
                    continue

                fvg.mitigated = True

                mitigation = Mitigation(
                    zone_type="FVG",
                    zone=fvg,
                    time=candle.time,
                    index=candle.index,
                )

                mitigations.append(mitigation)

                break

        return mitigations