"""Diagnostics meta-tests for the headless launch smoke test.

Spec scenario 6 requires a broken launch to fail the smoke test *and* report
the traceback. These tests run the real ``tests/test_smoke.py`` against a
throwaway copy of ``main.py`` so the diagnostic contract stays verified without
mutating the working tree.
"""

import subprocess
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SMOKE_TEST = ROOT / "tests" / "test_smoke.py"
TRACEBACK_HEADER = "Traceback (most recent call last)"


def _run_smoke_against(
    main_source: str, tmp_path: Path
) -> subprocess.CompletedProcess[str]:
    """Run the real smoke test in a throwaway repo whose main.py is ``main_source``."""
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_smoke.py").write_text(SMOKE_TEST.read_text())
    (tmp_path / "main.py").write_text(textwrap.dedent(main_source))
    return subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_smoke.py", "-q"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )


def test_broken_launch_reports_the_traceback(tmp_path: Path) -> None:
    result = _run_smoke_against("raise RuntimeError('boom at startup')\n", tmp_path)

    assert result.returncode != 0, result.stdout + result.stderr
    assert "1 failed" in result.stdout
    assert TRACEBACK_HEADER in result.stdout
    assert "RuntimeError: boom at startup" in result.stdout


def test_alive_launch_with_traceback_on_stderr_reports_it(tmp_path: Path) -> None:
    noisy_but_alive = """\
        import sys
        import time

        sys.stderr.write("Traceback (most recent call last):\\n")
        sys.stderr.write("RuntimeError: noisy but alive\\n")
        sys.stderr.flush()
        time.sleep(30)
        """
    result = _run_smoke_against(noisy_but_alive, tmp_path)

    assert result.returncode != 0, result.stdout + result.stderr
    assert "1 failed" in result.stdout
    assert "RuntimeError: noisy but alive" in result.stdout
