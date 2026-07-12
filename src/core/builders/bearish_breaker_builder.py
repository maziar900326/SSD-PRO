from src.models.breaker import Breaker


class BearishBreakerBuilder:

    def build(
        self,
        candles,
        order_blocks,
        bearish_bos=None,
        bearish_choch=None,
    ):
        """
        Build Bearish Breaker Blocks.

        Parameters
        ----------
        candles : list[Candle]

        order_blocks : list[OrderBlock]

        bearish_bos : list
            Optional list of Bearish BOS.

        bearish_choch : list
            Optional list of Bearish CHOCH.

        Returns
        -------
        list[Breaker]
        """

        breakers = []

        bearish_bos = bearish_bos or []
        bearish_choch = bearish_choch or []

        confirmations = bearish_bos + bearish_choch

        if not confirmations:
            return breakers

        for order_block in order_blocks:

            if getattr(order_block, "direction", None) != "BULLISH":
                continue

            for confirmation in confirmations:

                if confirmation.index <= order_block.index:
                    continue

                breaker = Breaker(
                    direction=Breaker.BEARISH,
                    upper_price=order_block.upper_price,
                    lower_price=order_block.lower_price,
                    time=confirmation.time,
                    index=confirmation.index,
                )

                breakers.append(breaker)

                break

        return breakers