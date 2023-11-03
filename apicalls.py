import requests


def get_data(detailed:bool=False):
    """ gets daily data from open meteo api, detailed to add current and hourly data"""
    if detailed:
        api_url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.61092&longitude=3.87723&current=temperature_2m,relativehumidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weathercode,cloudcover,windspeed_10m,winddirection_10m,windgusts_10m&hourly=temperature_2m,relativehumidity_2m,precipitation_probability,precipitation,rain,showers,snowfall,weathercode,cloudcover,visibility,windspeed_10m,winddirection_10m,windgusts_10m&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant&timezone=Europe%2FBerlin"
    else:
        api_url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.61092&longitude=3.87723&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,windspeed_10m_max,winddirection_10m_dominant"

    response = requests.get(api_url)
    return response.json()

