# ORDER BLOCK SPECIFICATION

---

# Purpose

Order Block Engine is responsible for detecting institutional order blocks.

Order Blocks are generated after significant impulsive moves and are later
used by:

- Entry Engine
- Market Analyzer
- Risk Engine

Order Blocks are NOT standalone entry signals.

They must be confirmed by:

- BOS
- CHOCH
- Liquidity
- Fair Value Gap

---

# Version

Current Version : v0.5.0

---

# Supported Types

Current Version supports:

- Bullish Order Block
- Bearish Order Block

Future versions:

- Breaker Block
- Mitigation Block
- Reclaimed Order Block

---

# Bullish Order Block

Definition

The last bearish candle before a bullish impulse.

Conditions

- Previous trend is bearish or ranging
- Strong bullish impulse
- BOS or CHOCH confirmation
- Valid liquidity context

Result

Bullish Order Block

---

# Bearish Order Block

Definition

The last bullish candle before a bearish impulse.

Conditions

- Previous trend is bullish or ranging
- Strong bearish impulse
- BOS or CHOCH confirmation
- Valid liquidity context

Result

Bearish Order Block

---

# Validation Rules

A valid Order Block must satisfy:

- Impulse exists
- Market Structure confirms
- Liquidity confirms

Version 0.5.0

Mitigation is NOT checked yet.

Mitigation will be implemented in v0.5.1