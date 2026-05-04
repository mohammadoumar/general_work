# General Bash Work

A lightweight README for organizing, writing, testing, and maintaining general bash scripts and utilities.

## Overview
Quick collection of conventions, examples, and tools to keep bash projects portable, readable, and robust.

## Repository layout
- bin/        — executable scripts intended for direct use
- lib/        — reusable shell libraries and helpers
- tests/      — test scripts and fixtures
- docs/       — documentation and examples
- examples/   — usage demos and sample inputs
- README.md   — this file

## Prerequisites
- Bash 4.x+ (or target minimum documented)
- coreutils, grep, sed, awk (common POSIX utilities)
- Optional: git, shellcheck, bats (for tests)

## Conventions
- Start scripts with a shebang: #!/usr/bin/env bash
- Fail early: set -euo pipefail
- Use functions with clear names
- Return meaningful exit codes (0 success, non-zero error)
- Prefer POSIX-compatible constructs when portability is required
- Document public functions and script usage (help flag)

## Recommended header template
```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

progname="$(basename "$0")"

usage() {
    cat <<EOF
Usage: $progname [options]

Description...
Options:
    -h|--help    Show help
EOF
}
```

## Logging and errors
- Use simple logging helpers:
```bash
info()  { printf '%s\n' "$*"; }
warn()  { printf 'WARN: %s\n' "$*"; }
error() { printf 'ERROR: %s\n' "$*"; exit 1; }
```
- Send debug logs to stderr when appropriate

## Input validation
- Validate arguments and environment early
- Quote variables: "$var"
- Check commands availability: command -v <tool> >/dev/null

## Portability tips
- Avoid bashisms if targeting /bin/sh
- Use printf instead of echo for predictable output
- Prefer $(...) over backticks

## Testing and linting
- Use shellcheck to catch common issues:
    shellcheck scripts/*.sh
- Use bats or shunit2 for automated tests:
    tests/run-tests.sh

## Examples
- Running a script:
    ./bin/myscript.sh -f input.txt
- Sourcing a library:
    source "$(dirname "${BASH_SOURCE[0]}")/../lib/common.sh"

## CI suggestions
- Run shellcheck, unit tests, and linting in CI
- Cache dependencies and artifacts for speed

## Contributing
- Follow the existing style and test your changes
- Add examples and tests for new behavior
- Create small, focused commits with clear messages

## License
MIT — include a LICENSE file for full terms.

## Further reading
- Bash Guide: https://www.gnu.org/software/bash/manual/
- ShellCheck: https://www.shellcheck.net/
