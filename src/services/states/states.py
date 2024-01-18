from dataclasses import dataclass


@dataclass
class SupplierClienState:
    viewstate: str
    generator: str
    eventvalidation: str
