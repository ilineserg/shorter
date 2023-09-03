import logging
from abc import ABC
from abc import abstractmethod
from contextlib import asynccontextmanager
from typing import Any
from typing import ContextManager
from typing import Generator
from typing import Generic
from typing import Type
from typing import TypeVar

from sqlalchemy import select, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from shorter.database.base import Base


logger = logging.getLogger(__name__)

TDbModel = TypeVar('TDbModel', bound=Base)
TEntityModel = TypeVar('TEntityModel')


class BaseRepository(ABC):

    @abstractmethod
    def add(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def get_one(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError()


class SqlAlchemyRepository(Generic[TDbModel, TEntityModel], BaseRepository, ABC):

    def __init__(self, session_factory: Type[AsyncSession]):
        self.session_factory = session_factory

    @asynccontextmanager
    async def session(self) -> ContextManager[Generator[AsyncSession, None, None]]:
        session: AsyncSession = self.session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            await session.rollback()
            raise
        finally:
            await session.close()

    @abstractmethod
    def get_db_model_class(self) -> Type[TDbModel]:
        raise NotImplementedError()

    @abstractmethod
    def create_object(self, db_object: TDbModel) -> TEntityModel:
        raise NotImplementedError()

    def create_db_object(self, **kwargs: Any) -> TDbModel:
        return self.get_db_model_class()(**kwargs)

    async def add(self, **kwargs: Any) -> TEntityModel:
        db_object = self.create_db_object(**kwargs)
        async with self.session() as session:
            session.add(db_object)
            await session.commit()
            return self.create_object(db_object=db_object)

    async def get_one(self, **kwargs: Any) -> TEntityModel | None:
        async with self.session() as session:
            try:
                db_object = (await session.execute(
                    select(self.get_db_model_class()).filter_by(**kwargs),
                )).scalar_one()
                return self.create_object(db_object=db_object)
            except NoResultFound:
                return None

    async def delete(self, **kwargs: Any) -> None:
        async with self.session() as session:
            await session.execute(
                delete(self.get_db_model_class()).filter_by(**kwargs),
            )
            await session.commit()
