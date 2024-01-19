from dataclasses import dataclass

from src.repositories.base import BaseRepository


@dataclass
class RepositoriesPair:
    slave: BaseRepository
    master: BaseRepository
