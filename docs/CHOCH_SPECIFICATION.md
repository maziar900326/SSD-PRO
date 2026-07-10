# CHOCH (Change Of Character) Specification

Version: 1.0

Status: Draft

---

# Purpose

Detect the first confirmed change in market character after an established trend.

CHOCH is the earliest confirmation that market structure has shifted.

---

# Inputs

- Candles
- Swings
- Trend
- Structures
- BOS List

---

# Outputs

List[CHOCH]

Each CHOCH contains:

- Direction
- Broken Structure
- Break Candle
- Time
- Price

---

# Bullish CHOCH

Conditions:

1. Current trend is DOWN

2. Last confirmed external structure is LL

3. Price closes ABOVE the latest LH

4. Break must occur after the LH is confirmed

Result:

Bullish CHOCH

---

# Bearish CHOCH

Conditions:

1. Current trend is UP

2. Last confirmed external structure is HH

3. Price closes BELOW the latest HL

4. Break occurs after HL confirmation

Result:

Bearish CHOCH

---

# Difference Between BOS And CHOCH

BOS

- Continues existing trend

CHOCH

- Changes existing trend

---

# Rules

Rule 1

Only candle CLOSE confirms CHOCH.

Rule 2

Wicks do not confirm CHOCH.

Rule 3

One break equals one CHOCH.

Rule 4

CHOCH must always reference a valid Structure.

Rule 5

CHOCH cannot occur before Structure confirmation.

---

# Edge Cases

- Equal High

- Equal Low

- Double Break

- Gap Break

- Missing Structure

- Range Market

---

# Required Tests

- Bullish CHOCH

- Bearish CHOCH

- No Break

- Wick Only

- Equal High

- Equal Low

- Double Break

- Range Market

---

# Future Compatibility

This engine will be used by:

- Liquidity Engine

- Order Block Engine

- Fair Value Gap Engine

- Entry Engine