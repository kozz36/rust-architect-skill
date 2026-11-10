---
name: rust-architect
description: "Trigger: Rust architecture, ownership, async, Cargo, CLI/TUI, backend, library, no_std, unsafe or FFI. Design and verify context-specific Rust changes."
license: Apache-2.0
metadata:
  author: "kozz36"
  version: "1.0.0"
---

## Activation Contract

Use for Rust design, implementation, debugging or review involving ownership,
concurrency, compatibility or platform boundaries. Inspect the actual workspace;
do not infer a framework, runtime or project type from the language alone.
Load only relevant profiles below, combining them when targets overlap.

## Hard Rules

- Preserve existing contracts and unrelated changes. Prefer the smallest safe
  design; justify dependencies, cloning, shared state and unsafe individually.
- Separate MSRV, edition, selected toolchain, target and feature requirements.
  Check API stabilization and dependency compatibility, not only manifest claims.
- Never replace an ownership diagnosis with mechanical cloning or lifetime
  extension. Trace who owns, borrows, mutates and outlives each boundary.
- Treat unsafe and FFI as explicit contracts, not performance shortcuts.
  Never promise soundness from tests, Miri, layout annotations or panic catching.
- Run only available, authorized checks. Do not install tools, fetch dependencies
  or access the network automatically. Label proposed, executed, failed and
  unavailable verification separately; never invent results.

## Decision Gates

| Context | Load and decide |
|---------|-----------------|
| CLI, terminal, paths, pipes | CLI/TUI: stream and cleanup contracts |
| Async service, concurrency, blocking | Backend: admission and cancellation |
| Public API, features, compatibility | Library: consumer obligations and MSRV |
| Embedded, no_std, unsafe, FFI | Systems: target and safety contracts |
| Version-sensitive or disputed claim | Sources: scope, date and primary evidence |

## Execution Steps

1. Inspect manifests, target layout, lockfile policy, tests and local conventions.
   Infer Cargo targets, including coexisting library and binaries. Record the
   requested behavior and constraints before proposing an architecture.
2. Read the relevant local references. Identify ownership, error, concurrency,
   compatibility and trust boundaries; ask only for unresolved consequential
   choices, not facts available in the repository.
3. Compare a minimal existing-pattern solution with alternatives only where the
   tradeoff matters. State allocation, synchronization and dependency costs;
   avoid universal framework, error-type or lint policies.
4. Implement a bounded change with behavior-level tests where runnable. Preserve
   public behavior and rejected-input invariants. Probe failure, cancellation,
   shutdown and target/feature boundaries applicable to the change.
5. Select authorized checks matching the claimed configuration. Distinguish host
   checks from target coverage and structural checks from runtime evidence.
   Recheck moving API claims against the pinned toolchain when possible;
   otherwise state the evidence gap rather than silently upgrading requirements.

## Output Contract

Return the decision and rationale, changed surfaces, compatibility assumptions,
verification commands with observed outcomes, and remaining risks. State edition,
MSRV and selected toolchain separately; use unknown or unchanged rather than
silently conflating them. For proposed commands, include `Tool availability:
verified/unavailable/unknown; authorization: granted/needed/unknown`, including
when no commands ran; never infer availability from permission. For CLI/TUI
changes, state terminal-restoration behavior or why it
is not applicable. Separate proposed checks from executed checks. Name unavailable
tools and untested targets; do not equate passing checks with exhaustive
correctness or soundness.

## References

- [CLI/TUI](references/cli-tui.md)
- [Backend](references/backend.md)
- [Library](references/library.md)
- [Systems](references/systems.md)
- [Sources and freshness](references/sources.md)
