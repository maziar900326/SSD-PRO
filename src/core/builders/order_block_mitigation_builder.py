from src.models.mitigation import Mitigation


class OrderBlockMitigationBuilder:

    def build(
        self,
        candles,
        order_blocks,
    ):
        """
        Detect mitigated Order Blocks.

        Parameters
        ----------
        candles : list[Candle]

        order_blocks : list[OrderBlock]

        Returns
        -------
        list[Mitigation]
        """

        mitigations = []

        for order_block in order_blocks:

            if getattr(order_block, "mitigated", False):
                continue

            for candle in candles:

                if candle.index <= order_block.index:
                    continue

                touched = (
                    candle.high >= order_block.lower_price
                    and
                    candle.low <= order_block.upper_price
                )

                if not touched:
                    continue

                order_block.mitigated = True

                mitigation = Mitigation(
                    zone_type="ORDER_BLOCK",
                    zone=order_block,
                    time=candle.time,
                    index=candle.index,
                )

                mitigations.append(mitigation)

                break

        return mitigations