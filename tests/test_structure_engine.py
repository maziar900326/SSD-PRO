import unittest

from src.models.swing import Swing
from src.core.structure_engine import StructureEngine


class TestStructureEngine(unittest.TestCase):

    def test_higher_high(self):

        swings = [
            Swing(0, "2024-01-01", 100, Swing.HIGH),
            Swing(1, "2024-01-02", 110, Swing.HIGH),
        ]

        structures = StructureEngine(swings).run()

        self.assertEqual(len(structures), 1)
        self.assertTrue(structures[0].is_hh)

    def test_lower_high(self):

        swings = [
            Swing(0, "2024-01-01", 120, Swing.HIGH),
            Swing(1, "2024-01-02", 100, Swing.HIGH),
        ]

        structures = StructureEngine(swings).run()

        self.assertEqual(len(structures), 1)
        self.assertTrue(structures[0].is_lh)

    def test_higher_low(self):

        swings = [
            Swing(0, "2024-01-01", 90, Swing.LOW),
            Swing(1, "2024-01-02", 95, Swing.LOW),
        ]

        structures = StructureEngine(swings).run()

        self.assertEqual(len(structures), 1)
        self.assertTrue(structures[0].is_hl)

    def test_lower_low(self):

        swings = [
            Swing(0, "2024-01-01", 95, Swing.LOW),
            Swing(1, "2024-01-02", 90, Swing.LOW),
        ]

        structures = StructureEngine(swings).run()

        self.assertEqual(len(structures), 1)
        self.assertTrue(structures[0].is_ll)


if __name__ == "__main__":
    unittest.main()