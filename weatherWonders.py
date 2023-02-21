worldTemps = [
    {'place': 'Antarctica', 'temp': -89.20},
    {'place': 'Russia', 'temp': -67.80},
    {'place': 'Greenland', 'temp': -66.10},
    {'place': 'Canada', 'temp': -63.00},
    {'place': 'China', 'temp': -58.00},
    {'place': 'United States', 'temp': -57.00},
    {'place': 'Mongolia', 'temp': -55.30},
    {'place': 'Kyrgyzstan', 'temp': -53.60},
    {'place': 'Sweden', 'temp': -52.60},
    {'place': 'Afghanistan', 'temp': -52.20},
    {'place': 'Finland', 'temp': -51.50},
    {'place': 'Norway', 'temp': -51.40},
    {'place': 'Italy', 'temp': -49.60},
    {'place': 'Austria', 'temp': -47.10},
    {'place': 'Turkey', 'temp': -46.40},
    {'place': 'Germany', 'temp': -45.90},
    {'place': 'North Korea', 'temp': -43.60},
    {'place': 'Estonia', 'temp': -43.50},
    {'place': 'Latvia', 'temp': -43.20},
    {'place': 'Lithuania', 'temp': -42.90},
    {'place': 'Belarus', 'temp': -42.20},
    {'place': 'Czech Republic', 'temp': -42.20},
    {'place': 'Armenia', 'temp': -42.00},
    {'place': 'Ukraine', 'temp': -41.90},
    {'place': 'Switzerland', 'temp': -41.80},
    {'place': 'Japan', 'temp': -41.00},
    {'place': 'France', 'temp': -41.00},
    {'place': 'Poland', 'temp': -41.00},
    {'place': 'Slovakia', 'temp': -41.00},
    {'place': 'Serbia', 'temp': -39.50},
    {'place': 'Romania', 'temp': -38.50},
    {'place': 'Bulgaria', 'temp': -38.30},
    {'place': 'Iceland', 'temp': -37.90},
    {'place': 'Chile', 'temp': -37.00},
    {'place': 'Iran', 'temp': -36.00},
]


def lookup_one(place):
    for i in worldTemps:
        if i['place'] == place:
            print('The minimum temperature in ' + str(place) + ' is: ', i['temp'])
            return i['temp']
    print('None')
    return None


def lookup_several(places):
    temps = []
    for place in places:
        temp = lookup_one(place)
        if temp is not None:
            temps.append(temp)
    return temps


place = input('Enter a nation (if multiple, separate by commas): ')
places = place.split(', ')
if len(places) == 1:
    lookup_one(place)
else:
    lookup_several(places)
