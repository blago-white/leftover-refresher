from src.config.settings import DealerSettings
from src.reports.transfer.article import Article
from src.reports.transfer.report import Report


def json_to_report(json: dict[str, list[dict[str, str | int]]]) -> Report:
    return Report(
        [json_to_article(article)
         for article in json[DealerSettings.STOCKS_INFO_DICT_KEY]
         ]
    )


def json_to_article(json: dict[str, str | int]) -> Article:
    return Article(
        article=json.get(DealerSettings.SKU_BODY_PARAM),
        leftover=json.get(DealerSettings.STOCKS_PRESENT_KEY)
    )
