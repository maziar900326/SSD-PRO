from src.models.mitigation import Mitigation


class BreakerMitigationBuilder:

    def build(
        self,
        candles,
        breakers,
    ):
        """
        Detect mitigated Breaker Blocks.

        Parameters
        ----------
        candles : list[Candle]

        breakers : list[Breaker]

        Returns
        -------
        list[Mitigation]
        """

        mitigations = []

        for breaker in breakers:

            if getattr(breaker, "mitigated", False):
                continue

            for candle in candles:

                if candle.index <= breaker.index:
                    continue

                touched = (
                    candle.high >= breaker.lower_price
                    and
                    candle.low <= breaker.upper_price
                )

                if not touched:
                    continue

                breaker.mitigated = True

                mitigation = Mitigation(
                    zone_type="BREAKER",
                    zone=breaker,
                    time=candle.time,
                    index=candle.index,
                )

                mitigations.append(mitigation)

                break

        return mitigations