from datetime import datetime, timedelta


weekdays_dict = {
  0:"Monday", 
  1:"Tuesday", 
  2:"Wednesday",
  3:"Thursday",
  4:"Friday",
  5:"Saturday",
  6:"Sunday"}

wmo_code_map:{
    0: 'clear sky',
    1: 'mainly clear', 
    2: 'partly cloudy', 
    3: 'overcast',
    45: 'fog', 48: 'depositing rime fog',
    51: 'light drizzle', 53: 'moderate drizzle', 55: 'dense drizzle',
    56: 'light freezing drizzle', 57: 'dense freezing drizzle',
    61: 'slight rain', 63: 'moderate rain', 65: 'heavy rain',
    66: 'light freezing rain', 67: 'dense freezing rain',
    71: 'slight snow fall', 73: 'moderate snow fall', 75: "heavy snow fall",
    77: 'snow grains',
    80: 'slight rain showers', 81: 'moderate rain showers', 82: 'violent rain showers',
    85: 'slight snow shower', 86: 'heavy snow showers',
    95: 'thunderstorm',
    96: 'thunderstorm with slight hail', 99: 'thunderstorm with heavy hail',
    #_UNKNOWN: 'unknown'
}


def get_sky(weather: str):
    if weather == "sun":
        return "http://www.clker.com/cliparts/5/3/a/3/1194989210401174033sun01.svg"
    elif weather == "scloudy":
        return "http://www.clker.com/cliparts/0/a/e/a/11949892041568310221cloudy01.svg"
    elif weather == "rain":
        return "http://www.clker.com/cliparts/4/2/0/7/11949892071155302510rain.svg"
    else:
        return None


def get_weekday(daily_data):
    """ takes daily data and returns the respective weekday"""
    return weekdays_dict[datetime.strptime(daily_data, '%Y-%m-%d').weekday()]


def convert_date(date:str, format):
    return datetime.strptime(date, format) + timedelta(hours=1)


def create_MD_weather_table(data):
    """takes data and creates markdown tables displaying it"""
    table = f"""| Today | {get_weekday(data['daily']['time'][1])}|{get_weekday(data['daily']['time'][2])}|{get_weekday(data['daily']['time'][3])}|
    |----|----|----|----|
    |good|good|nogood|good|"""
    return table

def create_MD_weather_table_alt(data):
    """Generates a Markdown table for weather data"""
    
    # Extract the dates and weather conditions
    weekdays = [get_weekday(day) for day in data['daily']['time'][1:4]]
    dates = [convert_date(x, '%Y-%m-%d').strftime('%d.%m.') for x
              in data['daily']['time']]
    #conditions = ['notgood','good','notgood','perfect']
    visuals = [f"({get_sky('sun')})", 
               f"({get_sky('sun')})", 
               f"({get_sky('rain')})",
               f"({get_sky('scloudy')})"]
    temp_max = [str(x) for x in data['daily']['temperature_2m_max']]
    temp_min = [str(x) for x in data['daily']['temperature_2m_min']]
    sunrise = [convert_date(x, '%Y-%m-%dT%H:%M').strftime('%H:%M') for x
               in data['daily']['sunrise']]
    sunset = [convert_date(x, '%Y-%m-%dT%H:%M').strftime('%H:%M') for x
              in data['daily']['sunset']]

    # Initialize the table header
    table = "| Today | " + " | ".join(weekdays) + " |\n"
    table += "| ---- | " + " | ".join(["----" for _ in weekdays]) + " |\n"

    # Create rows with dates
    table += "| " + " | ".join(dates) + " |\n"

    # Create rows with weather graphics
    table += f"| ![]" + " | ![]".join(visuals) + " |\n"

    # temperature
    table += f"| " + "° max |".join(temp_max) + "° max |\n"
    table += f"| " + "° min |".join(temp_min) + "° min |\n"

    # sunrise & -set
    table += f"| sunrise: " + "h | sunrise: ".join(sunrise) + "h |\n"
    table += f"| sunset: " + "h | sunset: ".join(sunset) + "h |\n"
    

    return table

# [get_weather_condition(condition) for condition in data['daily']['conditions'][1:4]]