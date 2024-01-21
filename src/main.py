import asyncio
import logging
import aiohttp

from src.config import config, settings
from src.controllers.dataclasses_ import RepositoriesPair
from src.controllers.reports import ArticlesLeftoversController
from src.reports.filters.tracked import TrackedAtriclesFilter
from src.repositories.dealer import DealerReportsRepository
from src.repositories.supplier import SupplierReportsRepository
from src.services.dealer import DeallerWebService
from src.services.supplier import SupplierWebService
from src.tracked.articles import TrackedArticlesListManager


async def _refresh_tracked_articles(service: DeallerWebService) -> list[str]:
    manager = TrackedArticlesListManager(dealer_service=service)

    await manager.refresh()


async def main(credentals: config.Credentals) -> None:
    async with aiohttp.ClientSession() as session:
        supplier_service = SupplierWebService(
            auth_credentals=credentals.supplier,
            aoihttp_session=session,
        )

        dealer_service = DeallerWebService(
            auth_credentals=credentals.dealer,
            aoihttp_session=session
        )

        await _refresh_tracked_articles(service=dealer_service)

        controller = ArticlesLeftoversController(
            repositories=RepositoriesPair(
                master=SupplierReportsRepository(
                    service=supplier_service,
                    reports_filter=TrackedAtriclesFilter()
                ),
                slave=DealerReportsRepository(service=dealer_service)
            ),
        )

        await controller.synchronize()


if __name__ == '__main__':
    logging.basicConfig(
        format=settings.LoggingSettings.LOG_FORMAT,
        level=settings.LoggingSettings.DEFAULT_LOGGING_MODE,
        filename=settings.LoggingSettings.LOG_FILE_PATH,
        filemode="w"
    )

    asyncio.run(main(
        credentals=config.load_config(
            path=settings.ConfigSettings.CONFIG_FILE_PATH
        )
    ))
