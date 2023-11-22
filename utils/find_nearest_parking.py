import utils.dp_api.db_commands as db
from math import sin, cos, sqrt, atan2, radians


async def find_nearest_parking(lat: float, lon: float):
    def pack(id_parking: int, dist: float):
        return id_parking, dist

    correct_points = []

    points = await db.select_all_parking()
    for point in points:
        if point.free_places != 0:
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
