import unittest

from src.core.mitigation_engine import MitigationEngine


class DummyOrderBlock:

    def __init__(self):
        self.direction = "BULLISH"
        self.upper_price = 1.1050
        self.lower_price = 1.1040
        self.index = 10
        self.mitigated = False


class DummyFVG:

    def __init__(self):
        self.direction = "BULLISH"
        self.upper_price = 1.1080
        self.lower_price = 1.1070
        self.index = 10
        self.mitigated = False


class DummyBreaker:

    def __init__(self):
        self.direction = "BULLISH"
        self.upper_price = 1.1110
        self.lower_price = 1.1100
        self.index = 10
        self.mitigated = False


class DummyCandle:

    def __init__(
        self,
        time,
        high,
        low,
        index,
    ):
        self.time = time
        self.high = high
        self.low = low
        self.index = index


class TestMitigationEngine(unittest.TestCase):

    def test_find_all(self):

        candles = [

            DummyCandle(
                time="2026-01-02",
                high=1.1120,
                low=1.1030,
                index=20,
            )

        ]

        engine = MitigationEngine(
            candles=candles,
            order_blocks=[DummyOrderBlock()],
            fvgs=[DummyFVG()],
            breakers=[DummyBreaker()],
        )

        mitigations = engine.find_all()

        self.assertEqual(
            len(mitigations),
            3,
        )


if __name__ == "__main__":
    unittest.main()