from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.sql import func
from ..config.db import Base


class Users(Base):

    __tablename__ = "users"

    id = Column("id", String, primary_key=True, unique=True, nullable=False)
    display_name = Column("display_name", String(255))
    email = Column("email", String(255), unique=True, nullable=False, index=True)
    photo_url = Column("photo_url", String(255), nullable=True)

    update_at = Column(
        "updated_at", TIMESTAMP(timezone=True), default=func.now(), onupdate=func.now()
    )
    created_at = Column("created_at", TIMESTAMP(timezone=True), default=func.now())
