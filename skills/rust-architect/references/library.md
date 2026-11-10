# Library: design for actual consumers

## Keep compatibility axes separate

Record MSRV (`rust-version`), edition, toolchain selection, compilation targets
and supported feature combinations independently. Edition 2024 requires at least
Rust 1.85; that does not require migrating every project. A library and binary
can coexist, so infer the targets and their separate requirements from Cargo.

`rust-version` declares intent, not proof that all resolved dependencies or used
APIs meet it. Check the selected dependency graph and the minimum compiler.
For example, `core::error::Error` stabilized in 1.81: do not offer it unqualified
for a no_std library promising 1.80. Choose a compatible design or explicitly
negotiate an MSRV change.

Resolver incompatible-rust-versions fallback prefers compatible dependencies;
it is not a guarantee that resolution, compilation or every workspace member
meets an MSRV. Resolver behavior depends on Cargo version/configuration (resolver
3 defaults to fallback). Inspect these instead of promising a manifest toggle
solves transitive compatibility. Respect lockfile and update policy.

## Public error APIs

`Error` requires Debug and Display; it does not universally require an enum or
Send + Sync + 'static. Select concrete types, opaque wrappers or enums according
to recovery, matching, extensibility and consumer constraints. Add bounds when
an actual transport/runtime/consumer requires them. Preserve useful sources.

`anyhow` supports downcasting; do not claim type erasure makes recovery impossible.
Application context and stable library error contracts serve different needs.
Avoid exposing implementation dependencies without a reason.

## Evolution and feature matrix

- Consider `#[non_exhaustive]` when initially designing extensible public types.
  Adding it later can itself break downstream exhaustive matches/construction;
  it is not a universally safe patch fix.
- Recommend additive Cargo features. Exceptional mutually exclusive features
  exist, but document invalid combinations and provide deliberate diagnostics.
- Derive the supported matrix: default, no-default-features, relevant individual
  and combined features, target-specific configurations, and MSRV where promised.
  Do not blindly demand all-features if exclusivity makes it invalid.
- Avoid universal claims that dependency warnings break consumers: Cargo commonly
  uses cap-lints for dependencies. Still probe the crate's own documented strict
  lint policy and direct-development builds where relevant.

## Evidence to request or run

Use public API/compile tests for compatibility promises when authorized and tools
exist. Check dependency necessity, feature leakage and target-specific std use.
Report unsupported combinations explicitly; a single host default build is not
proof of the full support matrix. Never install missing toolchains automatically.
