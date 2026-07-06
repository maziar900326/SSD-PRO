# BOS (Break Of Structure) Specification

## Purpose

The BOSEngine is responsible for detecting valid Break Of Structure
events based on confirmed market structure.

It does not detect trend.
It does not detect CHOCH.
It only detects BOS.

---

# Inputs

BOSEngine receives:

- Swing List
- Current Trend

---

# Outputs

BOSEngine returns:

List[BOS]

Each BOS represents one valid structure break.

---

# Bullish BOS

Requirements:

1. Current Trend is UPTREND

2. Market has a confirmed Higher Low (HL)

3. Price breaks the previous Higher High (HH)

4. Break is confirmed by candle close
   (V1 may ignore this confirmation)

---

# Bearish BOS

Requirements:

1. Current Trend is DOWNTREND

2. Market has a confirmed Lower High (LH)

3. Price breaks previous Lower Low (LL)

4. Break is confirmed by candle close
   (V1 may ignore this confirmation)

---

# Invalid BOS

No BOS should be generated when:

- Trend is RANGE

- Structure is incomplete

- Previous swing is not confirmed

- Break happens against trend

---

# Engine Responsibility

BOSEngine only detects BOS.

Trend detection belongs to TrendEngine.

CHOCH detection belongs to CHOCHEngine.