import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.models.swing import Swing
from src.models.trend import Trend
from src.core.bos_engine import BOSEngine


def main():

    swings = [
        Swing(0, None, 100, Swing.HIGH),
        Swing(1, None, 90, Swing.LOW),

        Swing(2, None, 110, Swing.HIGH),
        Swing(3, None, 100, Swing.LOW),

        Swing(4, None, 120, Swing.HIGH),
    ]

    trend = Trend(
        Trend.UPTREND,
        start_index=0,
        end_index=4
    )

    engine = BOSEngine(
        swings,
        trend
    )

    bos_list = engine.run()

    print("=" * 40)
    print("BOSEngine Test")
    print("=" * 40)
    print(f"BOS Count : {len(bos_list)}")

    for bos in bos_list:
        print(bos)

    print("=" * 40)


if __name__ == "__main__":
    main()