# Systems: separate platform and safety contracts

## no_std is not no allocation

Distinguish core-only, `alloc` with an allocator, and std-enabled builds. A host
build with default features disabled can still hide std leakage via dependencies,
feature unification, test harnesses or target configuration. Inspect the resolved
features and check a representative intended target where tools are available.
Do not claim no_std coverage from host tests alone. Record allocator, panic
handler, atomic availability and target limitations independently.

## Unsafe and FFI review gates

Require an explicit contract at each boundary, including caller obligations and
what the implementation guarantees. A nearby SAFETY explanation is a recommended
review policy, not a language proof. `unsafe_op_in_unsafe_fn` warns by default in
edition 2024; explicit unsafe blocks do not establish their own validity.

| Contract | Probe / review question |
|----------|-------------------------|
| Pointer validity | Is the pointer aligned, initialized, dereferenceable for the required range and lifetime, with valid provenance and aliasing? |
| Ownership | Who allocates, frees, transfers or borrows? Can another allocator or a second owner free it? |
| Layout | Which fields have a stable representation? `repr(C)` is not recursive and does not make String a C string or stable C interface. |
| ABI | Do calling convention, sizes, alignment and exported signatures match the foreign caller on each supported target? |
| Unwinding | May unwinding cross this ABI boundary? Account for Rust and foreign exceptions separately; choose an explicit boundary policy. |

Prefer an existing safe abstraction when it meets the constraints. For an FFI
string, define encoding, length/termination, ownership and release protocol;
never merely export a String field inside a repr(C) wrapper.

`catch_unwind` catches unwinding Rust panics, not panic=abort; it is neither a
universal FFI requirement nor a recovery mechanism for undefined behavior.
Do not promise it catches foreign exceptions or makes arbitrary boundaries safe.
Select an ABI/unwinding policy appropriate to the actual interface.

## Verification limits

Miri can detect many undefined behaviors in exercised paths and has malloc/free
shims; it does not support arbitrary foreign FFI and is not a proof of soundness.
Use it only if available and authorized, with its target/environment limitations
stated. Do not advertise unverified current-nightly support.

Fuzz state machines, operation sequences, invariants and protocol transitions,
not only byte parsers. Bound inputs and resources, choose an oracle, and preserve
reproducers when authorized. Tests, fuzzing, Miri and manual contract review are
complementary; none gives exhaustive safety or platform coverage.
