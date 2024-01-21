import json

from aiohttp.client import ClientSession

from src.config.config import DealerCredentals
from src.config.settings import DealerSettings
from src.reports.transfer.report import Report


class DealerApiMixin:
    @staticmethod
    def _get_leftovers_info_json() -> str:
        return json.dumps(
            {"filter": {}, "limit": DealerSettings.ARTICLES_LIMIT_PER_REQUEST})

    @staticmethod
    def _get_update_leftovers_json(report: Report) -> str:
        stocks = list()

        for article in report.articles:
            update_article_dict = {
                DealerSettings.OFFER_ID_PARAM: article.article,
                DealerSettings.NEW_STOCK_PARAM: article.leftover,
                DealerSettings.WAREHOUSE_PARAM: DealerSettings.WAREHOUSE_ID
            }

            stocks.append(update_article_dict)

        return json.dumps({DealerSettings.STOCKS_PARAM: stocks})

    @staticmethod
    def _get_all_articles_json() -> str:
        return json.dumps({
            "filter": {},
            "limit": 1000
        })

    @staticmethod
    def _get_articles_sku_json(offers: list[str]) -> str:
        return json.dumps({
            "offer_id": offers
        })


class DealerApiCredentalsMixin:
    _auth_credentals: DealerCredentals
    _session: ClientSession

    def _add_auth_headers(self):
        for header, value in self.__get_credentals_headers().items():
            self._session.headers.add(key=header, value=value)

    def __get_credentals_headers(self) -> dict[str, int | str]:
        return {
            DealerSettings.CLIENT_ID_HEADER: self._auth_credentals.client_id,
            DealerSettings.API_KEY_HEADER: self._auth_credentals.apikey
        }
