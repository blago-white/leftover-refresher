import subprocess
import time

from pathlib import Path, PosixPath

from src.config.settings import LoopSettings


def _get_root_path() -> PosixPath:
    return Path(__file__).resolve().parent


def _get_python_path() -> PosixPath:
    return "python"


def _get_task_path(root_path_: PosixPath) -> PosixPath:
    return root_path_ / "main.py"


def _run_refresh(*args):
    subprocess.run([
        _get_python_path(),
        str(_get_task_path(_get_root_path())),
        *args
    ])


def _run_refresh_stocks():
    _run_refresh("refresh", "--stocks")


def _run_refresh_articles():
    _run_refresh("refresh", "--articles")


if __name__ == '__main__':
    refreshes_counter = 0

    while True:
        refreshes_counter += 1

        if not refreshes_counter % 3:
            _run_refresh_articles()

        _run_refresh_stocks()

        time.sleep(LoopSettings.STOCKS_REFRESH_TIMEOUT_SEC)
