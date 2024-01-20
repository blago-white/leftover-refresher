from configparser import ConfigParser
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class SupplierCredentals:
    username: str
    password: str


@dataclass(frozen=True)
class DealerCredentals:
    client_id: int
    apikey: str


@dataclass(frozen=True)
class Credentals:
    supplier: SupplierCredentals
    dealer: DealerCredentals


def load_config(path: Path) -> Credentals:
    config = ConfigParser()
    config.read(path)

    dealer_config, supplier_config = config["Dealer"], config["Supplier"]

    return Credentals(
        supplier=SupplierCredentals(
            username=supplier_config.get("username"),
            password=supplier_config.get("password")
        ),
        dealer=DealerCredentals(
            client_id=dealer_config.get("clientid"),
            apikey=dealer_config.get("apikey")
        )
    )
