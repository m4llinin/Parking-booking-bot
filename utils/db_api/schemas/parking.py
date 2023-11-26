from sqlalchemy import Column, sql, Sequence, Integer, Float, ARRAY, BOOLEAN
from utils.db_api.db_gino import TimedBaseModel


class Parking(TimedBaseModel):
    __tablename__ = 'parking'
    id = Column(Integer, Sequence('parking_id_seq'), primary_key=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    all_places = Column(Integer, nullable=False)
    free_places = Column(Integer, nullable=False)
    places = Column(ARRAY(BOOLEAN), nullable=False)

    query: sql.select
