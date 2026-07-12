from src.core.builders.bullish_breaker_builder import (
    BullishBreakerBuilder,
)
from src.core.builders.bearish_breaker_builder import (
    BearishBreakerBuilder,
)


class BreakerEngine:

    def __init__(
        self,
        candles,
        order_blocks,
    ):
        self.candles = candles
        self.order_blocks = order_blocks

        self.bullish_builder = BullishBreakerBuilder()
        self.bearish_builder = BearishBreakerBuilder()

    def find_bullish(
        self,
        bullish_bos=None,
        bullish_choch=None,
    ):
        return self.bullish_builder.build(
            candles=self.candles,
            order_blocks=self.order_blocks,
            bullish_bos=bullish_bos,
            bullish_choch=bullish_choch,
        )

    def find_bearish(
        self,
        bearish_bos=None,
        bearish_choch=None,
    ):
        return self.bearish_builder.build(
            candles=self.candles,
            order_blocks=self.order_blocks,
            bearish_bos=bearish_bos,
            bearish_choch=bearish_choch,
        )

    def find_all(
        self,
        bullish_bos=None,
        bullish_choch=None,
        bearish_bos=None,
        bearish_choch=None,
    ):
        bullish = self.find_bullish(
            bullish_bos=bullish_bos,
            bullish_choch=bullish_choch,
        )

        bearish = self.find_bearish(
            bearish_bos=bearish_bos,
            bearish_choch=bearish_choch,
        )

        return bullish + bearish