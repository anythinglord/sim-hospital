import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENV = {**os.environ, "SDL_VIDEODRIVER": "dummy", "SDL_AUDIODRIVER": "dummy"}
ALIVE_WINDOW_SECONDS = 3


def test_main_launches_headless() -> None:
    proc = subprocess.Popen(
        [sys.executable, "main.py"],
        cwd=ROOT,
        env=ENV,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        time.sleep(ALIVE_WINDOW_SECONDS)
        rc = proc.poll()
    finally:
        proc.terminate()
        try:
            _, err = proc.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            _, err = proc.communicate()

    assert rc is None, f"main.py exited early (rc={rc}); captured stderr:\n{err}"
    assert "Traceback" not in err, err
