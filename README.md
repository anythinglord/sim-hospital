# Hospital Simulation

A simple hospital simulation built with pygame.

- press 'a' to admit a patient
- press 'd' to discharge a patient

## Requirements

- [uv](https://docs.astral.sh/uv/) — manages the Python interpreter and dependencies

Python is pinned to 3.12 (`.python-version`, `requires-python = ">=3.12,<3.13"`).
pygame 2.6.1 has no wheel for Python 3.14 (cp314), so do not run this project with it.

## Setup

```bash
uv python install 3.12
uv sync
```

## Run

```bash
uv run python main.py
```

Use `uv run`: it executes the game with the project virtualenv. A bare
`python main.py` may pick up a different system interpreter (uv does not
activate `.venv` automatically). If you prefer an activated shell:

```bash
source .venv/bin/activate
python main.py
```

## Test and lint

```bash
uv run pytest
uv run ruff check
```

The smoke test launches `main.py` headless for 3 seconds and passes only if the
process is still alive with no traceback. It never waits for exit: the game loop
runs until you close the window.

## Python 3.14 and pygame-ce

pygame 2.6.1 ships no cp314 wheel. If you must move to Python 3.14, `pygame-ce`
is a drop-in replacement (imports stay `import pygame`):

```bash
uv add pygame-ce
```

The pinned Python 3.12 setup above remains the supported path.
