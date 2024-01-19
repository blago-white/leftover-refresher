import json

from aiohttp.client import ClientSession

from src.config.config import DealerCredentals
from src.config.settings import DealerSettings

from ..transfer import UpdateReport


class DealerApiMixin:
    @staticmethod
    def _get_leftovers_info_json() -> str:
        return json.dumps({
            DealerSettings.SKU_BODY_PARAM: DealerSettings.TRACKED_SKUS
        })

    @staticmethod
    def _get_update_leftovers_json(update_report: UpdateReport) -> str:
        stocks = list()

        for update_article in update_report.articles:
            update_article_dict = {
                DealerSettings.OFFER_ID_PARAM: update_article.article_id,
                DealerSettings.NEW_STOCK_PARAM: update_article.leftover,
                DealerSettings.WAREHOUSE_PARAM: DealerSettings.WAREHOUSE_ID
            }

            stocks.append(update_article_dict)

        return json.dumps({DealerSettings.STOCKS_PARAM: stocks})


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
