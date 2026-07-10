# LIQUIDITY SPECIFICATION

---

# Purpose

Liquidity Engine is responsible for detecting areas where market participants'
stop-losses or pending orders are concentrated.

These areas are used later by:

- Order Block Engine
- Fair Value Gap Engine
- Entry Engine
- Market Analyzer

Liquidity itself is NOT an entry signal.

It is only a market context.

---

# Version

Current Version : v0.4.0
# Supported Liquidity Types

Version 0.4.0 supports:

- Equal High (EQH)
- Equal Low (EQL)

Future versions will include:

- Buy Side Liquidity (BSL)
- Sell Side Liquidity (SSL)
- Liquidity Sweep
- Liquidity Grab
# Equal High

Definition:

Two or more swing highs located at nearly the same price.

Conditions:

- Swing High
- Price Difference <= Tolerance
- No higher swing between them

Result:

Equal High Liquidity Zone
# Equal Low

Definition:

Two or more swing lows located at nearly the same price.

Conditions:

- Swing Low
- Price Difference <= Tolerance
- No lower swing between them

Result:

Equal Low Liquidity Zone