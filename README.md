# SSD Pro Trader

موتور تحلیل عرضه و تقاضا (Supply & Demand) بر اساس مفاهیم Sam Seiden و Smart Money Concept.

---

## اهداف پروژه

- اتصال به MetaTrader 5
- تحلیل خودکار بازار
- تشخیص روند
- تشخیص Rally، Drop و Base
- تشخیص Supply و Demand Zone
- تشخیص Fresh Zone
- امتیازدهی زون‌ها
- تولید سیگنال معاملاتی
- بک‌تست
- ژورنال معاملاتی

---

# Version History

## Version 0.1
تاریخ: 2026-07-02

### امکانات
- اتصال به MetaTrader 5
- دریافت داده‌های کندل
- نمایش DataFrame
- آماده‌سازی ساختار پروژه

---

## Version 0.2
تاریخ: 2026-07-02

### امکانات
- ساخت کلاس Candle
- ساخت Candle Engine
- تبدیل DataFrame به Candle Object
- محاسبه:
  - Bullish / Bearish
  - Body
  - Upper Wick
  - Lower Wick
  - Range

---

## Version 0.3 (در حال توسعه)

### برنامه
- Trend Engine
- تشخیص HH
- تشخیص HL
- تشخیص LH
- تشخیص LL
- تشخیص روند بازار

---

## نسخه‌های آینده

- Base Detector
- Rally Detector
- Drop Detector
- Supply Detector
- Demand Detector
- Fresh Zone
- Score Engine
- Signal Engine
- Backtest Engine
- Trading Journal
- Dashboard
## Version 0.4

### Added
- CandleEngine
- SwingEngine
- Swing High Detection
- Swing Low Detection
- Swing Test

Status:
Working ✅
# Version 0.4 (Stable)

## Added
- MT5Loader
- DataLoader
- Candle Model
- CandleEngine
- SwingEngine
- Swing Detection
- Unit Tests

## Refactor
- Standardized method names:
  - DataLoader.load()
  - MT5Loader.load()
  - CandleEngine.build()
  - SwingEngine.find_swings()

Status: ✅ Stable