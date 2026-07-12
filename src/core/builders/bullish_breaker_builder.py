from src.models.breaker import Breaker


class BullishBreakerBuilder:

    def build(
        self,
        candles,
        order_blocks,
        bullish_bos=None,
        bullish_choch=None,
    ):
        """
        Build Bullish Breaker Blocks.

        Parameters
        ----------
        candles : list[Candle]

        order_blocks : list[OrderBlock]

        bullish_bos : list
            Optional list of Bullish BOS.

        bullish_choch : list
            Optional list of Bullish CHOCH.

        Returns
        -------
        list[Breaker]
        """

        breakers = []

        bullish_bos = bullish_bos or []
        bullish_choch = bullish_choch or []

        confirmations = bullish_bos + bullish_choch

        if not confirmations:
            return breakers

        for order_block in order_blocks:

            if getattr(order_block, "direction", None) != "BEARISH":
                continue

            for confirmation in confirmations:

                if confirmation.index <= order_block.index:
                    continue

                breaker = Breaker(
                    direction=Breaker.BULLISH,
                    upper_price=order_block.upper_price,
                    lower_price=order_block.lower_price,
                    time=confirmation.time,
                    index=confirmation.index,
                )

                breakers.append(breaker)

                break

        return breakers