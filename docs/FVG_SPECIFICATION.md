# Fair Value Gap (FVG)

## Purpose

The Fair Value Gap (FVG) module detects market imbalances created by strong impulsive price movements.

This module provides bullish and bearish FVG detection that can later be used by:

- Order Blocks
- Mitigation
- Entry Engine
- Market Analyzer

---

## Definition
## Definition

A Fair Value Gap (FVG) is a price imbalance created by a strong impulsive movement.

The imbalance exists when three consecutive candles leave an untraded price range between the first and the third candle.

Bullish FVG

Candle1.high < Candle3.low

Bearish FVG

Candle1.low > Candle3.high

The middle candle represents the impulsive displacement that creates the imbalance.
## Detection Rules

The engine scans every three consecutive candles.

Bullish FVG

Condition

Candle1.high < Candle3.low

Gap

Upper Boundary = Candle3.low

Lower Boundary = Candle1.high

Bearish FVG

Condition

Candle1.low > Candle3.high

Gap

Upper Boundary = Candle1.low

Lower Boundary = Candle3.high

Only completed candles are evaluated.

The engine ignores incomplete market data.
## Bullish FVG

A Bullish Fair Value Gap is formed when:

Candle1.high < Candle3.low

The price range between:

Candle1.high

and

Candle3.low

is considered an imbalance.

The middle candle should represent a strong bullish displacement.

The gap remains valid until price fully mitigates the imbalance.
## Bearish FVG

A Bearish Fair Value Gap is formed when:

Candle1.low > Candle3.high

The price range between:

Candle3.high

and

Candle1.low

is considered an imbalance.

The middle candle should represent a strong bearish displacement.

The gap remains valid until price fully mitigates the imbalance.
## Validation Rules

A detected Fair Value Gap is considered valid when:

- Three consecutive completed candles are available.
- The gap size is greater than zero.
- The first and third candles satisfy the bullish or bearish condition.
- The middle candle represents an impulsive movement.
- Invalid or incomplete candles are ignored.

Future versions may include additional validation such as:

- Minimum gap size
- Volume confirmation
- ATR confirmation
- Trend confirmation
- BOS / CHOCH confirmation
## Future Improvements

Future versions of the FVG Engine may include:

- Mitigation detection
- Partial mitigation
- Consequent Encroachment (CE)
- Premium / Discount filtering
- Order Block association
- Liquidity association
- Multi-timeframe FVG detection
- Gap expiration logic
- Volume and ATR filters
## Output Model

Each detected Fair Value Gap should provide:

- Direction
- Upper Boundary
- Lower Boundary
- Creation Time
- Creation Index
- Mitigated Status

Example

Bullish FVG

Upper Boundary : 1.10540

Lower Boundary : 1.10485

Direction : Bullish

Mitigated : False