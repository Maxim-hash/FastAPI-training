from datetime import datetime, timezone
from sqlalchemy import JSON, Boolean, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Role(Base):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    permissions: Mapped[dict] = mapped_column(JSON)

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    registered_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey(Role.id))
    email: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False)