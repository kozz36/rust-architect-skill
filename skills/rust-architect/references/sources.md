# Sources and freshness

Use this ledger to locate primary semantics, not to impose an upgrade policy.
The completed research used agy Gemini 3.8 Flash High, independently challenged
by Astra with one cross-refutation round. Its observation cut-off was 2026-11-10.
This artifact preserves those findings and the primary locators inspected during
research. Assembly did not repeat live network verification; the dates below
identify research observations, not a fresh link-check or immutable archive.

The research observed official stable **1.99.1**, published **2026-10-15**.
That is a historical snapshot, not a minimum supported version or a claim about
what is latest when this skill runs. Publication date is distinct from the
observation date. Live documentation may now describe newer APIs; consult pinned
version docs and stabilization annotations before making an MSRV claim.

## Primary source ledger

Each observation date below refers to the inherited research cut-off, not an
independent worker fetch. Sections identify the claims to recheck when relevant.

| Primary URL | Section / claim | Kind | Observed |
|-------------|-----------------|------|----------|
| https://blog.rust-lang.org/2026/10/15/Rust-1.99.1/ | Official release announcement | Publication 2026-10-15 | 2026-11-10 |
| https://static.rust-lang.org/dist/channel-rust-stable.toml | Stable channel matched the announcement; compiler date differs from distribution date | Live channel manifest | 2026-11-10 |
| https://doc.rust-lang.org/edition-guide/rust-2024/index.html | Edition 2024, Rust 1.85 baseline | Live edition guide | 2026-11-10 |
| https://doc.rust-lang.org/cargo/reference/rust-version.html | MSRV declaration and support expectations | Live Cargo reference | 2026-11-10 |
| https://doc.rust-lang.org/cargo/reference/resolver.html | Rust-version fallback, resolver versions, feature unification | Live Cargo reference | 2026-11-10 |
| https://doc.rust-lang.org/core/error/trait.Error.html | Debug/Display requirements; stabilization in 1.81 | Live API docs | 2026-11-10 |
| https://doc.rust-lang.org/std/cell/struct.RefCell.html | Send/Sync implementations and runtime borrowing | Live API docs | 2026-11-10 |
| https://docs.rs/tokio/latest/tokio/macro.select.html#cancellation-safety | read is cancellation-safe; read_exact and write_all are not | Live upstream API docs | 2026-11-10 |
| https://docs.rs/tokio/latest/tokio/task/fn.spawn_blocking.html | Abort and shutdown limitations | Live upstream API docs | 2026-11-10 |
| https://docs.rs/anyhow/latest/anyhow/struct.Error.html | Downcasting and context | Live upstream API docs | 2026-11-10 |
| https://doc.rust-lang.org/cargo/reference/semver.html | Non-exhaustive changes and compatibility | Live Cargo reference | 2026-11-10 |
| https://doc.rust-lang.org/cargo/reference/features.html | Additive features, mutually exclusive features | Live Cargo reference | 2026-11-10 |
| https://doc.rust-lang.org/std/env/fn.args_os.html | Non-Unicode arguments | Live API docs | 2026-11-10 |
| https://doc.rust-lang.org/reference/type-layout.html | repr(C), field layout and representation limits | Live language reference | 2026-11-10 |
| https://doc.rust-lang.org/nomicon/ffi.html | ABI, ownership, unwinding boundaries | Live official unsafe guide | 2026-11-10 |
| https://github.com/rust-lang/miri | Supported operations, FFI limitations and non-proof status | Live upstream project documentation | 2026-11-10 |
| https://doc.rust-lang.org/rustc/lints/levels.html | cap-lints and dependency lint behavior | Live compiler reference | 2026-11-10 |
| https://rust-fuzz.github.io/book/ | Fuzz targets, invariants and operational limits | Live upstream tooling guide | 2026-11-10 |

## How to use the evidence

- Treat API and language contracts as official semantics within their documented
  version and configuration. Do not infer platform guarantees from one example.
- Treat additive features, minimal dependencies, bounded admission, and explicit
  safety explanations as design recommendations unless the project mandates them.
- Treat evaluation criteria as proposed skill policy, not observed model behavior.
- Recheck moving claims only with available, authorized access. If unavailable,
  report the stale or unverified claim rather than claiming current support.
- Prefer the project's selected toolchain documentation over latest docs when
  diagnosing compatibility. No exhaustive source or platform coverage is claimed.
