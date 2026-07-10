# SSD-PRO Project Rules

## Development Workflow

1. Every new feature must start with a Specification.
2. Every Model must have Unit Tests.
3. Every Engine must have Integration Tests.
4. No feature is complete without documentation.
5. Every release must have a Git tag.
6. Development is done on feature branches only.
7. The `main` branch must always remain stable.
8. All GitHub Actions checks must pass before merging.

---

## Code Style

- Use clear and descriptive class names.
- Keep Builders focused on one responsibility.
- Keep Engines as coordinators only.
- Avoid duplicated logic.
- Prefer composition over inheritance.

---

## Testing

- Every Builder must have Unit Tests.
- Every Engine must have Integration Tests.
- Tests must be deterministic.
- Factories should be used for reusable test data.

---

## Versioning

Semantic Versioning is used:

- Major → Breaking changes
- Minor → New features
- Patch → Bug fixes

Example:

v0.4.1
v0.5.0
v1.0.0