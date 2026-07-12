from src.core.builders.order_block_mitigation_builder import (
    OrderBlockMitigationBuilder,
)
from src.core.builders.fvg_mitigation_builder import (
    FVGMitigationBuilder,
)
from src.core.builders.breaker_mitigation_builder import (
    BreakerMitigationBuilder,
)


class MitigationEngine:

    def __init__(
        self,
        candles,
        order_blocks=None,
        fvgs=None,
        breakers=None,
    ):
        self.candles = candles

        self.order_blocks = order_blocks or []
        self.fvgs = fvgs or []
        self.breakers = breakers or []

        self.order_block_builder = OrderBlockMitigationBuilder()
        self.fvg_builder = FVGMitigationBuilder()
        self.breaker_builder = BreakerMitigationBuilder()

    def find_order_blocks(self):
        return self.order_block_builder.build(
            candles=self.candles,
            order_blocks=self.order_blocks,
        )

    def find_fvgs(self):
        return self.fvg_builder.build(
            candles=self.candles,
            fvgs=self.fvgs,
        )

    def find_breakers(self):
        return self.breaker_builder.build(
            candles=self.candles,
            breakers=self.breakers,
        )

    def find_all(self):

        mitigations = []

        mitigations.extend(
            self.find_order_blocks()
        )

        mitigations.extend(
            self.find_fvgs()
        )

        mitigations.extend(
            self.find_breakers()
        )

        return mitigations