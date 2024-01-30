#!/usr/bin/env python

import sys
import asyncio
import logging

from src import run_refreshing, refresh_tracked_articles_list
from src.config import config, settings


def main():
    if (len(sys.argv) < 3
            or not sys.argv[1] == "refresh"
            or sys.argv[2] == "help"):
        return

    if sys.argv[2] == "--stocks":
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
