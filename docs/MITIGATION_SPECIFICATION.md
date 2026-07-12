# Mitigation

## Purpose

The Mitigation module detects when previously identified Smart Money zones have been revisited by price.

Mitigation is used to determine whether a zone remains active or has already been consumed by the market.

This module supports mitigation detection for:

- Order Blocks
- Fair Value Gaps
- Breaker Blocks

The output of this module will be used by the Entry Engine to filter invalid trading zones.
## Definition

Mitigation occurs when price revisits a previously identified Smart Money zone.

A mitigated zone has already interacted with price and therefore may lose its validity as a future trading opportunity.

Each supported zone defines mitigation differently:

- Order Block:
  Price revisits the Order Block after its creation.

- Fair Value Gap:
  Price fills the imbalance.

- Breaker Block:
  Price returns to the Breaker zone after confirmation.

A mitigated zone should be marked but preserved for historical analysis.
## Mitigation Rules

### Order Block Mitigation

An Order Block is mitigated when price revisits its price range after formation.

---

### Fair Value Gap Mitigation

A Fair Value Gap is mitigated when price fully fills the imbalance.

Partial fills do not invalidate the Fair Value Gap.

---

### Breaker Block Mitigation

A Breaker Block is mitigated when price revisits the Breaker zone after confirmation.

The first valid revisit marks the Breaker as mitigated.
## Validation Rules

A zone is NOT mitigated when:

- Price does not touch the zone.
- Price only approaches the zone.
- The revisit occurred before the zone was created.

Additional validation:

- A zone can only be mitigated once.
- Once mitigated, the zone remains marked for historical analysis.
- Mitigated zones should not be considered valid by the Entry Engine.
## Future Improvements

Future versions may include:

- Partial Mitigation Detection
- Multi-Timeframe Mitigation
- Volume Confirmation
- Time-Based Expiration
- Zone Strength Reduction
- Mitigation Statistics
- Automatic Zone Cleanup
- Entry Engine Integration