from typing import Dict
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, DeclarativeBase

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class A(Base):
    __tablename__ = "a"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    bs = relationship("B", back_populates="a", cascade="all, delete-orphan")

    def update_bs(self, b_data: Dict[str, str]):
        bs = []
        for b in b_data:
            bs.append(B(a_id=self.id, **b))  # type: ignore
        setattr(self, "bs", bs)
        db.session.commit()

    def to_dict(self):
        return {"id": self.id, "name": self.name, "bs": [b.to_dict() for b in self.bs]}

    def __repr__(self):
        return (
            f"<A(id={self.id}, name={self.name}, bs={[b.__repr__ for b in self.bs]})>"
        )


class B(Base):
    __tablename__ = "b"
    a_id = Column(Integer, ForeignKey("a.id"), primary_key=True)
    name = Column(String(50), primary_key=True)
    id = Column(Integer)

    a = relationship("A", back_populates="bs")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "a_id": self.a_id}

    def __repr__(self):
        return f"<B(id={self.id}, name={self.name}, a_id={self.a_id})>"


db = SQLAlchemy(model_class=Base)
