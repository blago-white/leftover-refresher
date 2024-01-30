#!/usr/bin/env python

import sys
import asyncio
import logging
import argparse

from src import run_refreshing, refresh_tracked_articles_list
from src.config import config, settings


def get_args_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Leftovers Refresher",
        description="""
        This is a script for synchronizing product balances on different platforms, 
        saving hundreds of hours spent on synchronizing data between platforms
        """,
        epilog="Follow creator - https://github.com/blago-white"
    )

    parser.add_argument("refresh",
                        help="Refresh data, stocks or list of tracked articles" 
                             "depending on the options")
    parser.add_argument("help")
    parser.add_argument("--articles",
                        help="Refresh only list of tracked articles")
    parser.add_argument("--stocks",
                        help="Refresh stocks of tracked articles")

    return parser


def main():
    args = get_args_parser().parse_args()

    if args.help or not args.refresh:
        get_args_parser().print_help()
        return

    if args.stocks:
        asyncio.run(run_refreshing(
            credentals=config.load_config(
                path=settings.ConfigSettings.CONFIG_FILE_PATH
            )
        ))

    elif args.articles:
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
