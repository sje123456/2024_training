# city_functions.py

def city_country(city, country, population=None):
    if population:
        return f"{city}, {country} - population {population}"
    else:
        return f"{city}, {country}"
