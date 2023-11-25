from sqlalchemy import Column, String, sql, Sequence, Integer, BigInteger, ForeignKey, Time, Date
from utils.dp_api.db_gino import TimedBaseModel


class Booking(TimedBaseModel):
    __tablename__ = 'booking'
    id = Column(Integer, Sequence('bookings_id_seq'), primary_key=True)
    id_parking = Column(Integer, ForeignKey('parking.id'), nullable=False)
    user_id = Column(BigInteger, nullable=False)
    vehicle_number = Column(String(200), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    status = Column(String, default='waiting')

    query: sql.select
