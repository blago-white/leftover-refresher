from crontab import CronTab
from pathlib import Path, PosixPath

import sys

sys.path.append(str(Path(__file__).resolve().parent))

import _utils


def _get_root_path() -> PosixPath:
    return Path(__file__).resolve().parent.parent.parent


def _get_python_path() -> PosixPath:
    return Path(__file__).resolve().parent.parent.parent / "venv/bin/python"


def _get_task_path(root_path_: PosixPath) -> PosixPath:
    return root_path_ / "main.py"


def _add_job(tab: CronTab):
    job = tab.new(
        command=f"{_get_python_path()} {_get_task_path(root_path_=_get_root_path())}"
    )

    job.minute.every(5)

    tab.write()


if __name__ == "__main__":
    tab = CronTab(user=_utils.get_username())

    _add_job(tab=tab)
