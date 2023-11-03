

def get_sky(weather: str):
    if weather == "sun":
        return "http://www.clker.com/cliparts/5/3/a/3/1194989210401174033sun01.svg"
    elif weather == "scloudy":
        return "http://www.clker.com/cliparts/0/a/e/a/11949892041568310221cloudy01.svg"
    elif weather == "rain":
        return "http://www.clker.com/cliparts/4/2/0/7/11949892071155302510rain.svg"
    else:
        return None