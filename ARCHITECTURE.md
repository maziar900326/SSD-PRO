# SSD-PRO Architecture

## Goal

Build a modular trading analysis engine based on Supply & Demand and Smart Money concepts.

---

## Project Layers

### Data

Responsible for loading market data.

- MT5Loader

---

### Models

Market objects.

- Candle
- Swing
- BOS (future)
- CHOCH (future)
- Zone (future)

---

### Core

Business logic.

- CandleEngine
- SwingEngine
- BOSEngine (future)
- CHOCHEngine (future)

---

### Tests

Unit tests for every engine.

---

## Development Roadmap

### Phase 1
- MT5 Connection
- Candle Model
- Swing Detection

### Phase 2
- BOS
- CHOCH
- Trend
- Supply & Demand

### Phase 3
- Signal Engine
- Risk Management

### Phase 4
- Scanner
- Backtest
- Dashboard
- Alerts