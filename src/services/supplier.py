from src.config.config import SupplierCredentals, SupplierAuthResources

from .default import DefaultWebService
from .mixins import sessions


class SupplierWebService(sessions.SupplierSessionWebServiceMixin, DefaultWebService):
    def __init__(self, auth_sources: SupplierAuthResources):
        self._auth_resources = auth_sources

    def get(self) -> bytes:
        pass
