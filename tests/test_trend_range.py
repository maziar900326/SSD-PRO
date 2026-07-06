import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.models.swing import Swing
from src.core.trend_engine import TrendEngine


def main():

    # نه Higher High داریم و نه Lower High
    # بنابراین باید RANGE تشخیص داده شود.
    swings = [
        Swing(0, None, 100, Swing.HIGH),
        Swing(1, None, 90, Swing.LOW),
        Swing(2, None, 95, Swing.HIGH),
        Swing(3, None, 95, Swing.LOW),
    ]

    engine = TrendEngine(swings)

    trend = engine.run()

    print("=" * 40)
    print("TrendEngine Range Test")
    print("=" * 40)
    print(trend)
    print("=" * 40)


if __name__ == "__main__":
    main()