from src.config.settings import DealerSettings

from .config import ARTICLES_KEY_NAME


def serialize_api_list(api_articles_list: dict) -> dict[str, str]:
    api_articles_list = api_articles_list["result"]["items"]

    return {
        ARTICLES_KEY_NAME: [
            str(article[DealerSettings.OFFER_ID_PARAM])
            for article in api_articles_list
        ]
    }
