import unittest
from datetime import datetime

from src.core.liquidity_engine import LiquidityEngine
from src.models.swing import Swing


class TestLiquidityEngine(unittest.TestCase):

    def test_engine_returns_liquidity(self):

        swings = [

            Swing(
                index=1,
                time=datetime.now(),
                price=1.2050,
                swing_type=Swing.HIGH
            ),

            Swing(
                index=3,
                time=datetime.now(),
                price=1.2052,
                swing_type=Swing.HIGH
            ),

            Swing(
                index=6,
                time=datetime.now(),
                price=1.1000,
                swing_type=Swing.LOW
            ),

            Swing(
                index=9,
                time=datetime.now(),
                price=1.1002,
                swing_type=Swing.LOW
            )

        ]

        engine = LiquidityEngine(
            swings,
            tolerance=0.0005
        )

        result = engine.build()

        self.assertEqual(len(result), 2)

        self.assertTrue(result[0].is_eqh)

        self.assertTrue(result[1].is_eql)


if __name__ == "__main__":
    unittest.main()