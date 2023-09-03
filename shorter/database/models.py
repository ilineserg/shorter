from sqlalchemy import Column, String

from .base import Base


class Url(Base):
    __tablename__ = 'urls'

    short_url = Column(String(), primary_key=True)
    source_url = Column(String(), index=True)
