# Premium / Discount

## Purpose

The Premium / Discount module calculates the relative price position within a valid market range.

The range is defined by the most recent confirmed swing high and swing low.

The module divides the range into three regions:

- Premium
- Equilibrium
- Discount

This information is used by the Entry Engine to determine whether buying or selling is favorable according to Smart Money Concepts.
## Definition

Premium and Discount are calculated using the most recent confirmed trading range.

The range is defined by:

- Confirmed Swing High
- Confirmed Swing Low

The midpoint of the range is called Equilibrium.

Price locations are classified as:

- Premium:
  Above Equilibrium.

- Equilibrium:
  The exact midpoint of the range.

- Discount:
  Below Equilibrium.

The Premium / Discount calculation is independent of trend direction and only depends on the selected market range.
## Calculation Rules

The trading range is calculated using:

Range = Swing High - Swing Low

The Equilibrium is calculated as:

Equilibrium = Swing Low + (Range / 2)

Price classification:

- Premium:
  Current Price > Equilibrium

- Equilibrium:
  Current Price == Equilibrium

- Discount:
  Current Price < Equilibrium

The calculated zones remain valid until a new confirmed trading range is established.
## Validation Rules

A Premium / Discount calculation is valid only when:

- Both Swing High and Swing Low are confirmed.
- Swing High is greater than Swing Low.
- The trading range is greater than zero.
- Current Price is within or near the selected trading range.

Invalid calculations:

- Missing Swing High.
- Missing Swing Low.
- Zero trading range.
- Negative trading range.

When a new confirmed trading range is established, all Premium / Discount levels must be recalculated.
## Future Improvements

Future versions may include:

- Multi-Timeframe Premium / Discount
- Fibonacci Premium / Discount Levels
- Optimal Trade Entry (OTE) Zone
- Dynamic Range Detection
- Automatic Swing Selection
- Premium / Discount Statistics
- Liquidity-Aware Premium / Discount
- Entry Engine Integration