import datetime as dt

from sqlalchemy import (
    create_engine,
    Column,
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

DeclarativeBase = declarative_base()


def create_tables(engine):
    DeclarativeBase.metadata.create_all(engine)


def initialize_database(database_url):
    engine = create_engine(database_url)
    create_tables(engine)
    return engine


class Gazette(DeclarativeBase):
    __tablename__ = "gazettes"
    id = Column(Integer, primary_key=True)
    source_text = Column(Text)
    date = Column(Date)
    edition_number = Column(String)
    is_extra_edition = Column(Boolean)
    power = Column(String)
    file_checksum = Column(String)
    file_path = Column(String)
    file_url = Column(String)
    scraped_at = Column(DateTime)
    created_at = Column(DateTime, default=dt.datetime.utcnow)
    territory = relationship("Territory", back_populates="gazettes")
    territory_id = Column(String, ForeignKey("territories.id"))
    processed = Column(Boolean, default=False)
    __table_args__ = (UniqueConstraint("territory_id", "date", "file_checksum"),)


class Territory(DeclarativeBase):
    __tablename__ = "territories"
    id = Column(String, primary_key=True)
    name = Column(String)
    state_code = Column(String)
    state = Column(String)
    gazettes = relationship("Gazette", order_by=Gazette.id, back_populates="territory")
