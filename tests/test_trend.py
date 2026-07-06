import os
import sys

# اضافه کردن پوشه اصلی پروژه به مسیر پایتون
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.models.swing import Swing
from src.core.trend_engine import TrendEngine


def main():

    swings = [
        Swing(0, None, 100, Swing.LOW),
        Swing(1, None, 120, Swing.HIGH),
        Swing(2, None, 110, Swing.LOW),
        Swing(3, None, 130, Swing.HIGH),
    ]

    engine = TrendEngine(swings)

    trend = engine.run()

    print("=" * 40)
    print("TrendEngine Test")
    print("=" * 40)
    print(trend)
    print("=" * 40)


if __name__ == "__main__":
    main()