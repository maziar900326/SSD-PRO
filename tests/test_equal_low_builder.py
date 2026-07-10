import unittest
from datetime import datetime

from src.core.builders.equal_low_builder import EqualLowBuilder
from src.models.swing import Swing
from src.models.liquidity import Liquidity


class TestEqualLowBuilder(unittest.TestCase):

    def test_single_equal_low(self):

        swings = [

            Swing(
                index=2,
                time=datetime.now(),
                price=1.1000,
                swing_type=Swing.LOW
            ),

            Swing(
                index=6,
                time=datetime.now(),
                price=1.1002,
                swing_type=Swing.LOW
            )

        ]

        builder = EqualLowBuilder(
            swings,
            tolerance=0.0005
        )

        result = builder.build()

        self.assertEqual(len(result), 1)

        zone = result[0]

        self.assertTrue(zone.is_eql)

        self.assertEqual(zone.type, Liquidity.EQL)

        self.assertAlmostEqual(
            zone.upper_price,
            1.1002,
            places=4
        )

        self.assertAlmostEqual(
            zone.lower_price,
            1.1000,
            places=4
        )

        self.assertAlmostEqual(
            zone.center_price,
            1.1001,
            places=4
        )


if __name__ == "__main__":
    unittest.main()