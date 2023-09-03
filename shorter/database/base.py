from typing import cast

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.orm import declarative_base


def get_all_constraint_columns_names(constraint, _) -> str:
    return "_".join([
        column.name for column in constraint.columns.values()
    ])


naming_convention = {
    "all_constraint_columns_names": get_all_constraint_columns_names,
    "ix": "ix__%(table_name)s__%(all_constraint_columns_names)s",
    "uq": "uq__%(table_name)s__%(all_constraint_columns_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": "fk__%(table_name)s__%(all_constraint_columns_names)s__%(referred_table_name)s",
    "pk": "pk__%(table_name)s"
}
Base: DeclarativeMeta = cast(
    DeclarativeMeta,
    declarative_base(
        metadata=MetaData(naming_convention=naming_convention),
    ),
)
