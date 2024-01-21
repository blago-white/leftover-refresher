from src.config.settings import DealerSettings


def get_offers_ids(response: dict) -> list[str]:
    return [item[DealerSettings.OFFER_ID_PARAM]
            for item in response["result"]["items"]]
