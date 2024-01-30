#!/usr/bin/env python

import sys
import asyncio
import logging

from src import run_refreshing, refresh_tracked_articles_list
from src.config import config, settings


_HELP_STRING = """
Follow creator - https://github.com/blago-white

This is a script for synchronizing product balances on different platforms, 
saving hundreds of hours spent on synchronizing data between platforms

Example of run script -----------------------------------

./main.py refresh --articles

Arguments -----------------------------------------------

help           Show this help info

refresh        Refresh data, stocks or list of tracked articles 
               depending on the options

Options -------------------------------------------------


--articles     Refresh only list of tracked articles
--stocks       Refresh stocks of tracked articles

"""


def main():
    if (len(sys.argv) < 2) or (sys.argv[1] == "help"):
        print(_HELP_STRING)

    if not sys.argv[1] == "refresh":
        return

    elif sys.argv[2] == "--stocks":
        asyncio.run(run_refreshing(
            credentals=config.load_config(
                path=settings.ConfigSettings.CONFIG_FILE_PATH
            )
        ))

    elif sys.argv[2] == "--articles":
        asyncio.run(refresh_tracked_articles_list(
            dealer_credentals=config.load_config(
                path=settings.ConfigSettings.CONFIG_FILE_PATH
            ).dealer
        ))


if __name__ == '__main__':
    logging.basicConfig(
        format=settings.LoggingSettings.LOG_FORMAT,
        level=settings.LoggingSettings.DEFAULT_LOGGING_MODE,
        filename=settings.LoggingSettings.LOG_FILE_PATH,
        filemode="w"
    )

    main()
