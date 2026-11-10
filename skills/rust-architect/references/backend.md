# Backend: bound work and preserve protocol state

## Ownership and synchronization

Trace shared state across await points before selecting synchronization. Avoid
holding blocking mutex guards across suspension; choose message passing, short
critical sections or async synchronization according to actual access patterns.
`RefCell<T>` can be Send when T is Send, but is not Sync. `Arc<RefCell<T>>` does
not make shared mutable access thread-safe. Do not mechanically wrap everything
in Arc/Mutex or clone data to silence diagnostics; identify ownership first.

## Bound admission, not only execution

A semaphore acquired inside an unlimited stream of spawned tasks still permits
unbounded queued tasks and captured memory. Acquire capacity before spawning,
use a bounded queue with backpressure, or keep a bounded in-flight set. Define
rejection, queueing, fairness and shutdown behavior. Probe both task count and
retained bytes under overload; a concurrency limit alone is not a memory bound.

## Cancellation and deadlines

| Operation | Required decision |
|-----------|-------------------|
| Tokio `read` | Cancellation-safe in the documented select context; retain returned bytes and parsing state across iterations. |
| Tokio `read_exact` / `write_all` | Not cancellation-safe; cancellation may lose progress accounting after partial I/O. Do not simply retry an entire frame. |
| Timeout around framing | Keep a persistent buffer/cursor and a deadline for the whole logical operation; decide whether cancellation invalidates the connection. |
| Blocking work | `spawn_blocking` tasks cannot be aborted once started. Aborting a handle or timing out the wait does not stop that work. |

For blocking jobs, bound admission separately, use cooperative cancellation where
possible, and choose process isolation if hard termination is truly required.
Do not imply async runtime shutdown forcibly interrupts already running jobs.

Probe partial headers/bodies, timeout after progress, resumed parsing, duplicate
writes, peer disconnect and shutdown with pending jobs. Distinguish cancellation
of a future from cancellation of an external side effect or transaction.

## Error boundaries

Retain actionable context without exposing secrets. Classify retryable versus
permanent failures according to the protocol, not string matching alone. Select
runtime/framework and error tooling from project constraints, not a universal
stack. Report load/cancellation tests as proposed unless actually executed.
