import logging

from src.services.dealer import DeallerWebService

from ._serializers import serialize_api_list
from ._utils import save_tracked_articles
from .utils import get_tracked_articles_ids


class TrackedArticlesListManager:
    def __init__(self, dealer_service: DeallerWebService):
        self._service = dealer_service

    @property
    def offer_ids(self) -> list[str]:
        return get_tracked_articles_ids()

    async def refresh(self) -> None:
        result = await self._service.get()

        logging.debug("Tracked Articles Fetched")

        result = serialize_api_list(api_articles_list=result)

        save_tracked_articles(articles=result)

        logging.debug("Tracked Articles Saved")
