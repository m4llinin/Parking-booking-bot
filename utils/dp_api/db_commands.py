from asyncpg import UniqueViolationError

from utils.dp_api.schemas.booking import Booking
from utils.dp_api.schemas.parking import Parking


# Выбор одной брони
async def select_booking(user_id: int,
                         vehicle_number: str):
    booking = await Booking.query.where(Booking.user_id == user_id).where(
        Booking.vehicle_number == vehicle_number).gino.first()
    return booking


# Поиск броней от пользователя для этого автомобиля на всех парковках
async def find_booking_for_all_parking(user_id: int,
                                       vehicle_number: str):
    booking = await Booking.query.where(Booking.user_id == user_id).where(
        Booking.vehicle_number == vehicle_number).gino.first()
    if booking:
        return True
    return False


# Выбор всех броней пользователя
async def select_all_booking_for_user_id(user_id: int):
    booking = await Booking.query.where(Booking.user_id == user_id).gino.all()
    return booking


# Добавление брони True - добавлено, False - не добавлено
async def add_booking(id_parking: int,
                      user_id: int,
                      vehicle_number: str):
    try:
        if not await find_booking_for_all_parking(user_id, vehicle_number):
            booking = Booking(
                id_parking=id_parking,
                user_id=user_id,
                vehicle_number=vehicle_number
            )
            await booking.create()
            return True
        return False
    except UniqueViolationError:
        print("Бронь не добавлена")
        return False


# Удаление брони
async def delete_booking(id_parking: int,
                         user_id: int,
                         vehicle_number: str):
    try:
        booking = await select_booking(user_id, vehicle_number)
        if booking:
            await booking.delete()
    except UniqueViolationError:
        print("Бронь не удалена")


# Выбор парковки
async def select_parking(longitude: float,
                         latitude: float):
    parking = await Parking.query.where(Parking.latitude == latitude).where(Parking.longitude == longitude).gino.first()
    return parking


# Возвращает все парковки
async def select_all_parking():
    return await Parking.query.gino.all()


# Проверка существует ли такая парковка уже?
async def find_parking(longitude: float,
                       latitude: float):
    parking = await Parking.query.where(Parking.latitude == latitude).where(Parking.longitude == longitude).gino.first()
    if parking:
        return True
    return False


# Добавление парковки True - добавлено, False - не добавлено
async def add_parking(longitude: float,
                      latitude: float,
                      all_places: int):
    try:
        if not await find_parking(longitude, latitude):
            parking = Parking(
                longitude=longitude,
                latitude=latitude,
                all_places=all_places,
                free_places=all_places
            )
            await parking.create()
            return True
        return False
    except UniqueViolationError:
        print("Парковка не добавлена")
        return False
