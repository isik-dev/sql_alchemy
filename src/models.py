from typing import Optional, Annotated
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str_256
from enum import Enum
from datetime import datetime, timezone


intpk = Annotated[int, mapped_column(primary_key=True)]
createdAt = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updatedAt = Annotated[datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"), 
    onupdate=datetime.now(timezone.utc))]


# 1. Declarative way of declaring the Tables
class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    username: Mapped[str]


class Workload(Enum):
    parttime = "parttime"
    fulltime = "fulltime"

class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    title: Mapped[str_256]
    compensation: Mapped[Optional[int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey(column="workers.id", ondelete="CASCADE"))
    created_at: Mapped[createdAt]
    updated_at: Mapped[updatedAt]





# 2. Imperative way of declaring the Tables
metadata_obj = MetaData()


workers_table = Table(
    "workers",
    metadata_obj,
    Column(name="id", type_=Integer, primary_key=True),
    Column(name="username", type_=String),
)
