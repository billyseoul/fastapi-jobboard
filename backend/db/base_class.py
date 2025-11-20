from typing import Any
from xml.etree.ElementTree import QName

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: Any
    __name__: str

    metadata: MetaData

    @declared_attr
    def __tablename__(cls)->str:
        return cls.__name__.lower()