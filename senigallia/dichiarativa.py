from typing import List, Optional
from sqlalchemy import ForeignKey, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Base(DeclarativeBase):
    pass

class Provincia(Base):
    __tablename__ = "provincia"
    id: Mapped[str] = mapped_column(String(2), primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column(String(30), nullable=True)
    regione_id: Mapped[int] = mapped_column(ForeignKey("regione.id"), nullable=True)
    regione: Mapped["Regione"] = relationship(back_populates="province")
    residenti: Mapped[int] = mapped_column(nullable=True)
    kmq: Mapped[int] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f"Provincia(id={self.id!r}, nome={self.nome})"

class Regione(Base):
    __tablename__ = "regione"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False) 
    nome: Mapped[str] = mapped_column(String(30))
    province: Mapped[List["Provincia"]] = relationship(
        back_populates="regione", cascade="all, delete-orphan"
    )

from sqlalchemy import create_engine
engine = create_engine("mysql://root:root@localhost/italy")

Base.metadata.create_all(engine)