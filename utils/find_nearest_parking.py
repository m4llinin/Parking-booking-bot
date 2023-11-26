from aiogram.fsm.context import FSMContext
from math import sin, cos, sqrt, atan2, radians
from datetime import datetime

from utils.db_api.schemas.booking import Booking
import utils.db_api.db_commands as db


async def find_nearest_parking(lat: float, lon: float, state: FSMContext):
    def pack(id_parking: int, dist: float):
        return id_parking, dist

    correct_points = []
    data = await state.get_data()
    free_parking = await Booking.query.where(Booking.start_date != data['start_date']).gino.all()
    free_parking += await Booking.query.where(
        Booking.start_time != datetime.strptime(data['start_time'], "%H:%M")).gino.all()
    free_parking += await Booking.query.where(Booking.end_date != data['end_date']).gino.all()
    free_parking += await Booking.query.where(
        Booking.end_time != datetime.strptime(data['end_time'], "%H:%M")).gino.all()
    if not free_parking:
        free_parking = await db.select_all_parking()
    parking_id = set([parking.id for parking in free_parking])
    parking = [await db.select_parking(Id) for Id in parking_id]

    for point in parking:
        if point:
            lat2, lon2 = radians(lat), radians(lon)
            lat1, lon1 = radians(point.latitude), radians(point.longitude)

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            # Вычисление формулы гаверсинусов
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = 6371.0 * c
            correct_points.append(pack(point.id, distance))

    correct_points.sort(key=lambda x: x[-1])
    return correct_points[:10]
