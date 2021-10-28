travel_log = [
    {
        'country': 'United Kingdom',
        'cities_visited': ['London', 'Birmingham', 'Brighton'],
        'total_visits': 4
    },
    {
        'country': 'United States',
        'cities_visited': ['New York', 'Austin', 'San Fransisco'],
        'total_visits': 3
    }
]

def add_new_country(country, cities, visits):
    new_country = {}
    new_country['country'] = country
    new_country['cities_visited'] = cities
    new_country['total_visits'] = visits
    global travel_log
    travel_log.append(new_country)






add_new_country('Russia', ['moscow', 'Stalingrad'], 2)
print(travel_log)
