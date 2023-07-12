import re
import hashlib
import requests
import datetime


TOWNS = ['yaoundé', 'douala', 'buea', 'bafoussam', 'bamenda']


# Extract the metadata
def translate(text) -> (str, str):

    trajets = [
        (departure, arrival)
        for departure in TOWNS
        for arrival in TOWNS if departure != arrival
    ]

    for departure, arrival in trajets:
        data = re.findall(
            rf'(départ|departure)\W.*?\W(bus)\W.*?'
            rf'\W({departure})\W.*?\W({arrival})\W',
            text, re.IGNORECASE
        )
        if data:
            return departure, arrival


# Fetch data from the server
def query(departure, arrival, language):

    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

    form = {
        "api_key": b"rh8b2v4tLJ2avDBZ",
        "departure": departure.encode(),
        "arrival": arrival.encode(),
        "date": tomorrow.strftime("%d/%m/%y").encode(),
        "language": language.encode(),
        "version": b"1.0",
    }

    form["hash"] = hashlib.md5(b''.join(form.values())).hexdigest()

    r = requests.post("https://lohce.com/apiusers/gettravels", data=form)
    data = r.json()['api_return']

    return data


# Summarize the data
def summarize(data):

    available_trajets = {}

    for trajet in data:
        agency = trajet['name_agency']

        if agency not in available_trajets:
            available_trajets[agency] = {
                'seat_available_count': trajet['seat_available_count'],
                'departures': [],
                'webui_link': trajet['webui_link']
            }

        available_trajets[agency]["seat_available_count"] += trajet['seat_available_count']
        available_trajets[agency]["seat_available_count"] /= 2

        available_trajets[agency]['departures'].append(
            " ".join([trajet['departure_time'], trajet['standing_trip']]))

    # We take the agency who has the more available seat
    return sorted(
        available_trajets.items(),
        key=lambda x: x[1]['seat_available_count'])[-1]


# Execute user command
def execute(text, language) -> (bool, str):
    metadata = translate(text)

    if not metadata:
        return (False, None)

    data = query(*metadata, language)

    if not data:
        return (True, None)

    data = summarize(data)

    return (True, data)
