import asyncio
import logging
import pathlib
import time
import aiohttp

from src.config import config, settings
from src.controllers.dataclasses_ import RepositoriesPair
from src.controllers.managers.reports import ReportsPairManager
from src.controllers.reports import ArticlesLeftoversController
from src.repositories.dealer import DealerReportsRepository
from src.repositories.supplier import SupplierReportsRepository
from src.services.dealer import DeallerWebService
from src.services.supplier import SupplierLeftoversWebService


async def main(credentals: config.Credentals) -> None:
    async with aiohttp.ClientSession() as session:
        supplier_service = SupplierLeftoversWebService(
            auth_credentals=credentals.supplier,
            aoihttp_session=session
        )

        dealer_service = DeallerWebService(
            auth_credentals=credentals.dealer,
            aoihttp_session=session
        )

        controller = ArticlesLeftoversController(
            repositories=RepositoriesPair(
                master=SupplierReportsRepository(service=supplier_service),
                slave=DealerReportsRepository(service=dealer_service)
            ),
            repositories_manager_class=ReportsPairManager
        )

        await controller.synchronize()


def _get_config():
    return config.load_config(
        path=settings.ConfigSettings.CONFIG_FILE_PATH
    )


if __name__ == '__main__':
    logging.basicConfig(
        format=settings.LoggingSettings.LOG_FORMAT,
        level=settings.LoggingSettings.DEFAULT_LOGGING_MODE,
        filename=settings.LoggingSettings.LOG_FILE_PATH,
        filemode="w"
    )

    asyncio.run(main(
        credentals=_get_config()
    ))
