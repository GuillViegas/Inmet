from sqlalchemy import Column, DECIMAL, String, Date, Float
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from app import base


class Mensuration(base):
    __tablename__ = 'mensurations'

    station = Column(DECIMAL(5), ForeignKey("stations.omm"), nullable=False, primary_key=True)
    station_base = relationship("Station", backref="station_base")
    source = Column(String(15), primary_key=True)
    date = Column(Date, nullable=False, primary_key=True)
    tempMax = Column(Float)
    tempMin = Column(Float)
    tempAvg = Column(Float)
    evp = Column(Float)
    prec = Column(Float)
    insolation = Column(Float)
    humidity = Column(Float)
