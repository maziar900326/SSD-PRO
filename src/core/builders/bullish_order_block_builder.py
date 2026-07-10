from src.core.services.impulse_detector import ImpulseDetector
from src.models.order_block import OrderBlock


class BullishOrderBlockBuilder:
    """
    Detects Bullish Order Blocks.

    Version 0.5.0

    Rule:

    Last bearish candle before
    a strong bullish impulse.
    """

    def __init__(self, candles):
        self.candles = candles
        self.impulse_detector = ImpulseDetector()

    def build(self):

        order_blocks = []

        for i in range(len(self.candles) - 1):

            base = self.candles[i]
            impulse = self.candles[i + 1]

            if self._is_bullish_order_block(base, impulse):

                order_blocks.append(

                    OrderBlock(

                        block_type=OrderBlock.BULLISH,

                        base_candle=base,

                        impulse_candle=impulse,

                        upper_price=base.high,

                        lower_price=base.low

                    )

                )

        return order_blocks

    def _is_bullish_order_block(
        self,
        base,
        impulse
    ):

        if not base.bearish:
            return False

        return self.impulse_detector.is_bullish_impulse(
            base,
            impulse
        )