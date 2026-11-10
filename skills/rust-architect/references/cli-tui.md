# CLI/TUI: preserve stream and terminal contracts

## Choose the interface

- Inspect Cargo targets before restructuring: a package may contain both a
  reusable library and several binaries. Do not force a lib-versus-bin choice.
- Use `args_os` and OS/path types when arguments can contain non-Unicode paths.
  Choose Unicode parsing only where the argument contract requires text.
- Keep machine-readable stdout separate from diagnostics on stderr. Preserve
  existing exit codes and scripting behavior before adding interactive output.

## Handle failure and cleanup

| Boundary | Decision or probe |
|----------|-------------------|
| Closed output pipe | Handle BrokenPipe deliberately; probe a consumer that closes early, avoiding panic/backtrace pollution. Match the CLI's exit convention. |
| Raw mode / alternate screen | Establish a cleanup guard before interaction; restore on normal return and recoverable error. Probe interruption and failure during initialization. |
| Panic or forced termination | Do not promise guards run with panic=abort, process kill or power loss. Document recovery limits. |
| Redirected output | Detect terminal capabilities when relevant; avoid mandatory color, cursor controls and interactive prompts in pipes. |
| Input and rendering | Separate state transitions from rendering so deterministic state tests do not require a terminal. |

## Validate only what changed

Propose subprocess checks for exact stdout, stderr and exit status, plus path
round-tripping and broken-pipe handling when touched. Use a pseudo-terminal only
when available and authorized to probe terminal restoration and resize behavior.
Report manual terminal observations separately from automated state tests.

Do not prescribe a CLI or TUI framework. Reuse the project's parser, event loop
and cleanup abstractions unless evidence warrants a change. Avoid logging secrets
or full user paths merely to make error messages more detailed.
