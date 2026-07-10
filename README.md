# SSD-PRO

Smart Money Concepts Analysis Framework written in Python.

---

## Overview

SSD-PRO is a modular framework for detecting Smart Money Concepts (SMC) from market data.

The framework is designed with:

- Clean Architecture
- Builder Pattern
- Engine Pattern
- Test-Driven Development
- Specification-Driven Development

---

## Current Features

### Core

- Candle
- Swing
- Trend
- Structure

### Market Structure

- Break of Structure (BOS)
- Change of Character (CHOCH)
- Liquidity Detection

---

## Roadmap

- ✅ BOS Engine
- ✅ CHOCH Engine
- ✅ Liquidity Engine

Upcoming:

- Order Block
- Fair Value Gap
- Premium / Discount
- Entry Engine
- Risk Engine
- Market Analyzer

---

## Project Structure

```
src/
    core/
    models/

tests/

docs/
```

---

## Installation

```bash
pip install -e .
```

---

## Running Tests

```bash
python -m unittest discover tests
```

---

## Version

Current Version

```
v0.4.1
```

---

## License

MIT License