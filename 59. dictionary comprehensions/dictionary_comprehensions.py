# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}

# print(cities_in_F)
# print(cities_in_C)

# ---------------------------------------------------------------

# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {k: v for (k, v) in weather.items() if v == "sunny"}

# print(weather)
# print(sunny_weather)

# ---------------------------------------------------------------

# cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}

# print(cities)
# print(desc_cities)

# ---------------------------------------------------------------

def check_temp(temp):
    if temp >= 70:
        return "HOT"
    elif temp > 40:
        return "WARM"
    else:
        return "COLD"      

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}

print(cities)
print(desc_cities)