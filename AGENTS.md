# AGENTS.md -- holomesh-py

This repo is the Python client and CLI surface for HoloMesh. Agents should keep
it thin: Python code should expose HoloMesh coordination and HoloScript substrate
access rather than reimplementing ecosystem control-plane logic locally.

## HoloScript Tool Integration

- HoloScript source/tool surface: when Python clients need language, validation,
  compile, or spatial behavior, call the HoloScript MCP/tool surface instead of
  duplicating `.holo`, `.hsplus`, or `.hs` semantics.
- HoloKey/x402 custody: preserve HoloKey, x402, and seat wallet provenance for
  registration, paid access, team actions, and signed receipts.
- Umbrella/routeTask routing: route ambiguous cross-repo work through the
  HoloMesh room board and `routeTask` umbrella before creating a Python-only
  substitute.
- Triads/uAAL: use the competitor-paper-codebase triad and uAAL lens for
  changes that affect protocol, agent, or ecosystem architecture.
- HoloGate note: HoloGate is a docs umbrella term only; it does not replace
  concrete HoloKey, routeTask, triad/uAAL, MCP, or source-level proof.

## Git Hygiene

- Stage explicit files only.
- Do not commit credentials, local tokens, or `~/.holomesh/` material.
