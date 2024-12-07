from src.config.settings import DealerSettings
from src.reports.transfer.article import Article
from src.reports.transfer.report import Report


def json_to_report(json: dict[str, list[dict[str, str | int]]]) -> Report:
    return Report(
        [json_to_article(article) for article in json[
            DealerSettings.STOCKS_INFO_DICT_KEY
        ][
             DealerSettings.STOCKS_ITEMS_DICT_KEY
        ]]
    )


def json_to_article(json: dict) -> Article:
    leftover = json[DealerSettings.STOCKS_PARAM][-1][
        DealerSettings.STOCKS_PRESENT_KEY
    ]

    return Article(
        article=json.get(DealerSettings.OFFER_ID_PARAM),
        leftover=leftover
    )
