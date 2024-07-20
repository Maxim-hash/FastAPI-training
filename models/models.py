from datetime import datetime, timezone
from typing import Annotated
from sqlalchemy import JSON, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

intPrimaryKey = Annotated[int, mapped_column(primary_key=True)]
notNullableString = Annotated[String, mapped_column(nullable=False)]

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    permissions: Mapped[dict] = mapped_column(JSON)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"))
