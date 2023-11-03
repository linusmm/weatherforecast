from datetime import datetime


weekdays_dict = {
  1:"Monday", 
  2:"Tuesday", 
  3:"Wednesday",
  4:"Thursday",
  5:"Friday",
  6:"Saturday",
  7:"Sunday"}


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


def create_MD_weather_table(data):
    """takes data and creates markdown tables displaying it"""
    table = f"""
    | Today | {get_weekday(data['daily']['time'][])}
    """
    return
