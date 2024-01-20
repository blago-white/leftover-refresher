import asyncio
import time
import aiohttp
import pathlib

from src.config import config

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


if __name__ == '__main__':
    config_path = pathlib.Path(__file__).resolve().parent / "config/config.ini"

    start = time.time()

    asyncio.run(main(
        credentals=config.load_config(path=config_path)
    ))

    print(time.time() - start)
