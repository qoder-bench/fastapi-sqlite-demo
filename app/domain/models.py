from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, Integer, Text, text
from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):
    name: str = Field(sa_column=Column('name', Text))
    power: str = Field(sa_column=Column('power', Text))
    age: int = Field(sa_column=Column('age', Integer))
    id: Optional[int] = Field(default=None, sa_column=Column('id', Integer, primary_key=True))
    created_at: Optional[datetime] = Field(default=None, sa_column=Column('created_at', DateTime, server_default=text('current_timestamp')))
    updated_at: Optional[datetime] = Field(default=None, sa_column=Column('updated_at', DateTime, server_default=text('current_timestamp')))
