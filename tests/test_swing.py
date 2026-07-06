from src.data.mt5_loader import MT5Loader
from src.core.candle_engine import CandleEngine
from src.core.swing_engine import SwingEngine


# دریافت داده از MT5
loader = MT5Loader()
df = loader.load(bars=200)

# تبدیل DataFrame به Candle
candles = CandleEngine().build(df)

# پیدا کردن Swingها
engine = SwingEngine(candles)

highs, lows = engine.find_swings()

print("Swing Highs:", len(highs))
print("Swing Lows :", len(lows))

print()
print(highs[:10])
print(lows[:10])

loader.shutdown()