import json

from src.config.settings import DealerSettings
from .config import ARTICLES_KEY_NAME


def get_tracked_articles_ids() -> list[dict[str, str]]:
    with open(DealerSettings.TRACKED_ARTICLES_JSON_PATH) as file:
        json_articles = json.load(file)

    return json_articles[ARTICLES_KEY_NAME]
