from src.services.supplier import SupplierLeftoversWebService

from .base import BaseReadOnlyRepository


class SupplierReportsRepository(BaseReadOnlyRepository):
    _service: SupplierLeftoversWebService

    async def get_all(self):
        pass
