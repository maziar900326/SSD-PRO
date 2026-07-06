import MetaTrader5 as mt5

from src.data.mt5_loader import MT5Loader
from src.core.candle_engine import CandleEngine
from src.core.swing_engine import SwingEngine


def main():

    # دریافت داده از MT5
    loader = MT5Loader()

    df = loader.load(
        symbol="XAUUSD",
        timeframe=mt5.TIMEFRAME_M15,
        bars=100
    )

    # تبدیل DataFrame به Candle
    candles = CandleEngine.build(df)

    # پیدا کردن Swingها
    engine = SwingEngine(candles)
    swings = engine.find_swings()

    print("=" * 60)
    print("SSD-PRO | Swing Detection")
    print("=" * 60)

    print(f"Total Candles : {len(candles)}")
    print(f"Total Swings  : {len(swings)}")
    print()

    print("First 10 Swings")
    print("-" * 60)

    for swing in swings[:10]:
        print(swing)

    loader.shutdown()


if __name__ == "__main__":
    main()