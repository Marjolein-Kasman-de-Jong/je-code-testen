# Opdracht 11-1 Stad, land
# Opdracht 11-2 Bevolking

def make_city_country_string(city, country, population = ''):
    """ Return a formatted string containing city, country and population (optional) """
    if population:
        return (city + ', ' + country + ' - population: ' + str(population)).title()
    else:
        return (city + ', ' + country).title()
