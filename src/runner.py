import logging
import logging

import aiohttp

from src.config import config
from src.controllers.dataclasses_ import RepositoriesPair
from src.controllers.reports import ArticlesLeftoversController
from src.reports.filters.tracked import TrackedAtriclesFilter
from src.repositories.dealer import DealerReportsRepository
from src.repositories.supplier import SupplierReportsRepository
from src.services import dealer, supplier, base
from src.tracked.articles import TrackedArticlesListManager

__all__ = ["run_refreshing", "refresh_tracked_articles_list"]


async def run_refreshing(credentals: config.Credentals) -> None:
    async with aiohttp.ClientSession() as session:
        supplier_service = supplier.SupplierWebService(
            auth_credentals=credentals.supplier,
            aoihttp_session=session,
        )

        dealer_service = dealer.DeallerWebService(
            auth_credentals=credentals.dealer,
            aoihttp_session=session
        )

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


async def refresh_tracked_articles_list(
        dealer_credentals: config.DealerCredentals
) -> None:
    async with aiohttp.ClientSession() as session:
        logging.debug("Start refreshing tracked articles ids")

        service = dealer.DeallerWebService(auth_credentals=dealer_credentals,
                                           aoihttp_session=session)

        manager = TrackedArticlesListManager(dealer_service=service)

        await manager.refresh()

        logging.debug("End refreshing tracked articles ids")
