import unittest
from datetime import datetime

from src.core.builders.equal_high_builder import EqualHighBuilder
from src.models.swing import Swing
from src.models.liquidity import Liquidity


class TestEqualHighBuilder(unittest.TestCase):

    def test_single_equal_high(self):

        swings = [

            Swing(
                index=1,
                time=datetime.now(),
                price=1.2050,
                swing_type=Swing.HIGH
            ),

            Swing(
                index=5,
                time=datetime.now(),
                price=1.2052,
                swing_type=Swing.HIGH
            )

        ]

        builder = EqualHighBuilder(
            swings,
            tolerance=0.0005
        )

        result = builder.build()

        self.assertEqual(len(result), 1)

        zone = result[0]

        self.assertTrue(zone.is_eqh)

        self.assertEqual(zone.type, Liquidity.EQH)

        self.assertAlmostEqual(
            zone.upper_price,
            1.2052,
            places=4
        )

        self.assertAlmostEqual(
            zone.lower_price,
            1.2050,
            places=4
        )

        self.assertAlmostEqual(
            zone.center_price,
            1.2051,
            places=4
        )


if __name__ == "__main__":
    unittest.main()