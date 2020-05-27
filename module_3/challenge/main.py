import requests


def get_temperature(lat, lng):
    if type(lat) not in [int, float] or type(lng) not in [int, float]:
        raise TypeError('Latitude and longitude must be of int or float type.')
    if lat > 90 or lat < -90:
        raise ValueError('Latitude value must be between 90 and -90.')
    if lng > 180 or lng < -180:
        raise ValueError('Longitude value must be between 180 and -180.')
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)
    reponse = requests.get(url)
    data = reponse.json()
    temperature = data.get('currently').get('temperature')
    if not temperature:
        return
    return int((temperature - 32) * 5.0 / 9.0)
