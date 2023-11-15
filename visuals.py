from datetime import datetime, timedelta


weekdays_dict = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
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


def get_sky_wmo(wmo_code):
    """fct to get the according image for every kind of weather"""
    if wmo_code <= 3:
        return "(http://www.clker.com/cliparts/5/3/a/3/1194989210401174033sun01.svg)"
    elif (wmo_code > 40) & (wmo_code < 60):
        return (
            "(http://www.clker.com/cliparts/0/a/e/a/11949892041568310221cloudy01.svg)"
        )
    elif (wmo_code >= 60) & (wmo_code < 70):
        return "(http://www.clker.com/cliparts/4/2/0/7/11949892071155302510rain.svg)"
    elif (wmo_code >= 70) & (wmo_code < 80):
        return "(http://www.clker.com/cliparts/6/b/a/a/11954437221169142395snowfall_raoul_rene_melc_01.svg)"


def get_weekday(daily_data):
    """takes daily data and returns the respective weekday"""
    return weekdays_dict[datetime.strptime(daily_data, "%Y-%m-%d").weekday()]


def convert_date(date: str, format):
    """converts time to local time"""
    return datetime.strptime(date, format) + timedelta(hours=1)


def create_MD_weather_table_alt(data):
    """Generates a Markdown table for weather data using the above fuctions"""

    # Extract the dates and weather conditions
    weekdays = [get_weekday(day) for day in data["daily"]["time"][1:4]]
    dates = [
        convert_date(x, "%Y-%m-%d").strftime("%d.%m.") for x in data["daily"]["time"]
    ]
    graphics = [get_sky_wmo(x) for x in data["daily"]["weathercode"]]
    temp_max = [str(x) for x in data["daily"]["temperature_2m_max"]]
    temp_min = [str(x) for x in data["daily"]["temperature_2m_min"]]
    sunrise = [
        convert_date(x, "%Y-%m-%dT%H:%M").strftime("%H:%M")
        for x in data["daily"]["sunrise"]
    ]
    sunset = [
        convert_date(x, "%Y-%m-%dT%H:%M").strftime("%H:%M")
        for x in data["daily"]["sunset"]
    ]

    # table header
    table = "| Today | " + " | ".join(weekdays) + " |\n"
    table += "| ---- | " + " | ".join(["----" for _ in weekdays]) + " |\n"

    # dates
    table += "| " + " | ".join(dates) + " |\n"

    # weather graphics
    table += f"| ![]" + " | ![]".join(graphics) + " |\n"

    # temperature
    table += f"| " + "° max |".join(temp_max) + "° max |\n"
    table += f"| " + "° min |".join(temp_min) + "° min |\n"

    # sunrise & -set
    table += f"| sunrise: " + "h | sunrise: ".join(sunrise) + "h |\n"
    table += f"| sunset: " + "h | sunset: ".join(sunset) + "h |\n"

    return table
