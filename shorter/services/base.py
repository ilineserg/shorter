from shorter.repositories import BaseRepository


class BaseService:
    repository: BaseRepository

    def __init__(self, repository: BaseRepository) -> None:
        self.repository = repository
