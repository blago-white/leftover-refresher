from dataclasses import dataclass


@dataclass(frozen=True)
class SupplierCredentals:
    username: str
    password: str


@dataclass(frozen=True)
class SupplierAuthResources:
    credentals: SupplierCredentals
    loginurl: str


@dataclass(frozen=True)
class DealerCredentals:
    apikey: str
