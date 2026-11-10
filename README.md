# Rust architect skill

A standalone v1.0.0 skill for context-specific Rust architecture and review,
authored by **kozz36**, licensed under Apache-2.0. It provides a compact runtime
contract plus situational guidance, not a framework or a Rust tutorial.

## Install locally

1. Read `skills/rust-architect/SKILL.md`.
2. Copy the **entire** `skills/rust-architect/` folder, including `references/`,
   into your agent's documented local skill directory.
3. Confirm your agent discovers the frontmatter and can load the relative links.

Do not copy only SKILL.md. No installer is bundled; use the manual installation
steps above. Agent-specific discovery is not validated here; no global
configuration changes are required by this repo.

## Choose the relevant context

| Context | Supporting material |
|---------|---------------------|
| Commands and terminal interfaces | `references/cli-tui.md`: paths, streams, cleanup |
| Services and async work | `references/backend.md`: admission, framing, cancellation |
| Public libraries | `references/library.md`: MSRV, errors, features, compatibility |
| Systems and embedded interfaces | `references/systems.md`: no_std, allocation, unsafe/FFI |

Paths in this table are relative to `skills/rust-architect/`. Contexts may overlap;
a package can contain both library and binary targets. Load only relevant detail.
The core links the source ledger separately for disputed or moving claims.

## Behavioral examples and evaluation

- **Prompt:** "Wrap read_exact in a timeout and retry the frame."
  **Expected:** identify partial progress and require persistent framing state or
  connection invalidation, with a logical-operation deadline.
- **Prompt:** "Our no_std crate targets MSRV 1.80; use core::error::Error."
  **Expected:** flag stabilization in 1.81 and propose a compatible alternative
  or explicit MSRV negotiation, not a silent upgrade.
- **Prompt:** "Abort spawn_blocking after a timeout."
  **Expected:** explain that started blocking work continues; discuss bounded
  admission and cooperative cancellation or isolation as requirements warrant.

The examples above are proposed behaviors, not executed Rust tests.
`evaluations/cases.json` defines 12 adversarial model cases. A blind responder
loaded the skill and relevant references without
seeing the rubric; a separate verifier judged its recorded answers:

| Observation (2026-11-10) | Result |
|-------------------------|--------|
| [Initial responses](evaluations/observations/2026-11-10-sol.json) | 10/12 complete; compatibility-axis and CLI tool-status/cleanup omissions |
| [First correction](evaluations/observations/2026-11-10-sol-correction-1.json) | MSRV case passed; CLI tool availability still omitted |
| [Second correction](evaluations/observations/2026-11-10-sol-correction-2.json) | Remaining CLI omission passed |

The core's output contract was clarified between probes. Composite rubric coverage
is 12/12 across those observations, **not a single-run 12/12 on the final revision**
or proof of general agent compliance. Executor: `general-purpose-sol`; underlying
model ID was not captured. Independent judging used `gentle-ai-verify`.
There are no compiled Rust examples or Rust compiler/runtime results here.

## Verify the public artifact

From the repository root, run:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

The standard-library suite validates metadata, section order, local reference
containment/existence, profiles, source-ledger shape and evaluation schema.
It does not validate Rust semantics, model behavior, URL availability or exact
LLM token count. A word-based body-size estimate is only a heuristic.

## Freshness and limits

Research cut-off: **2026-11-10**, using agy Gemini and an independent Astra
challenge. See `skills/rust-architect/references/sources.md` for primary locators,
claim scopes and provenance limits. The observed official release 1.99.1
(publication 2026-10-15) is a snapshot, not a mandate. Live docs can change.
No unverified current-nightly support or exhaustive platform coverage is claimed.

Optional tools require availability and authorization. The skill never grants
permission to install, fetch dependencies or use the network. Passing structural
checks is not proof of Rust correctness, soundness or agent compliance. Behavioral
evaluations require an agent to load the skill and answer the cases, followed by
independent judging; no universal compliance guarantee is implied.
