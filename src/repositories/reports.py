from .base import BaseRepository
from src.services.base import BaseWebService


class ReportsRepository(BaseRepository):
    async def get(self, *args, **kwargs):
        raise NotImplementedError

    async def get_all(self):
        pass

    async def save(self, data):
        pass
