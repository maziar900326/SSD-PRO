from src.models.order_block import OrderBlock


class OrderBlockValidator:
    """
    Validates Order Blocks.

    Version 0.5.0

    Current Validation

    ✓ Order Block is valid
    ✓ Base candle exists
    ✓ Impulse candle exists

    Future Validation

    ✓ BOS
    ✓ CHOCH
    ✓ Liquidity
    ✓ FVG
    ✓ Premium / Discount
    ✓ Mitigation
    """

    def validate(self, order_block):

        if not isinstance(order_block, OrderBlock):
            return False

        if not order_block.is_valid:
            return False

        if order_block.base_candle is None:
            return False

        if order_block.impulse_candle is None:
            return False

        return True