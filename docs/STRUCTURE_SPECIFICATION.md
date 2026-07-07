# Structure Specification

## Purpose

This document defines how market structure is identified inside SSD-PRO.

This specification is the single source of truth for:

- StructureEngine
- BOSEngine
- CHOCHEngine
- LiquidityEngine
- OrderBlockEngine

No engine may redefine these rules.

---

# Structure Types

There are only four valid market structure states.

| Type | Meaning |
|------|----------|
| HH | Higher High |
| HL | Higher Low |
| LH | Lower High |
| LL | Lower Low |

---

# Higher High (HH)

A swing high is Higher High when:

Current High Price > Previous High Price

Example

High1 = 100

High2 = 110

Result

HH

---

# Lower High (LH)

A swing high is Lower High when:

Current High Price < Previous High Price

Example

High1 = 110

High2 = 105

Result

LH

---

# Higher Low (HL)

A swing low is Higher Low when:

Current Low Price > Previous Low Price

Example

Low1 = 90

Low2 = 95

Result

HL

---

# Lower Low (LL)

A swing low is Lower Low when:

Current Low Price < Previous Low Price

Example

Low1 = 95

Low2 = 90

Result

LL

---

# Comparison Rules

Highs are compared only with previous highs.

Lows are compared only with previous lows.

Never compare:

High ↔ Low

---

# Output

StructureEngine returns

List[Structure]

Example

HH

HL

HH

HL

HH

---

# Notes

StructureEngine never detects BOS.

StructureEngine never detects Trend.

StructureEngine only classifies swing structure.