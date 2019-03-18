import api


def save_stations():
    stations_data = api.get_station_by_id(None)
    # for station in stations_data


def save_static_data():
    save_stations()
    save_lines()