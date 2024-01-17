from .base import BaseWebService


class DefaultWebService(BaseWebService):
    async def get(self) -> bytes:
        pass

    async def post(self) -> bytes:
        pass
