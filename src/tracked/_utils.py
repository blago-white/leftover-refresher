import json

from src.config.settings import DealerSettings


def save_tracked_articles(articles: dict) -> None:
    with open(DealerSettings.TRACKED_ARTICLES_JSON_PATH, "w") as file:
        json.dump(articles, file)
