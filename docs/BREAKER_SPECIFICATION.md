# Breaker Block

## Purpose

The Breaker Block module detects failed Order Blocks that become powerful reversal zones.

Breaker Blocks are formed after market structure shifts and are widely used in Smart Money Concepts for high-probability trade entries.

This module provides bullish and bearish Breaker Block detection that integrates with:

- BOS
- CHOCH
- Order Blocks
- Fair Value Gaps
- Entry Engine
## Definition

A Breaker Block is a failed Order Block that becomes a support or resistance zone after a confirmed market structure shift.

A Bullish Breaker is created when:

- A Bearish Order Block fails.
- Price breaks above the Order Block.
- A bullish BOS or CHOCH confirms the reversal.

A Bearish Breaker is created when:

- A Bullish Order Block fails.
- Price breaks below the Order Block.
- A bearish BOS or CHOCH confirms the reversal.

A Breaker Block is considered stronger when it aligns with:

- Fair Value Gap
- Liquidity Sweep
- Premium / Discount Zones
## Detection Rules

### Bullish Breaker

A Bullish Breaker is valid when:

1. A valid Bearish Order Block exists.
2. Price closes above the Order Block.
3. A bullish BOS or CHOCH confirms the market structure shift.
4. The previous Bearish Order Block becomes a support zone.

---

### Bearish Breaker

A Bearish Breaker is valid when:

1. A valid Bullish Order Block exists.
2. Price closes below the Order Block.
3. A bearish BOS or CHOCH confirms the market structure shift.
4. The previous Bullish Order Block becomes a resistance zone.
## Validation Rules

A Breaker Block is considered invalid when:

- The original Order Block has not failed.
- No BOS or CHOCH confirms the structure shift.
- Price never closes beyond the Order Block.
- The Breaker is immediately invalidated by an opposite market structure shift.

A valid Breaker should remain active until:

- It is mitigated.
- It is invalidated by a new confirmed market structure change.
## Future Improvements

Future versions may include:

- Breaker Strength Scoring
- Volume Confirmation
- Multi-Timeframe Breaker Detection
- Fair Value Gap Confluence
- Liquidity Sweep Confirmation
- Premium / Discount Filtering
- Breaker Retest Detection
- Entry Signal Generation