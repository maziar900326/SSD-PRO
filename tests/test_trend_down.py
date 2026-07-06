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

    # Lower High + Lower Low
    swings = [
        Swing(0, None, 120, Swing.HIGH),
        Swing(1, None, 100, Swing.LOW),
        Swing(2, None, 110, Swing.HIGH),
        Swing(3, None, 90, Swing.LOW),
    ]

    engine = TrendEngine(swings)

    trend = engine.run()

    print("=" * 40)
    print("TrendEngine Downtrend Test")
    print("=" * 40)
    print(trend)
    print("=" * 40)


if __name__ == "__main__":
    main()