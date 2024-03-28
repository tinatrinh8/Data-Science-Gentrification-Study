import requests
import json

from shapely import Point

# geocoding using the Mapbox API
# starter code: https://gist.github.com/thisismattmiller/9f21fd370b784adfe2593e2e2e784b3a
access_token = json.load(open('mapbox_key.json'))


def geocode(address_string):
    payload = {
        'types': 'address',
        'access_token': access_token,
        'country': 'CA',
        'proximity': '-79.3832,43.6532'
    }
    # lookfor = "305	SOUTH KINGSWAY"
    postal = address_string[-3:] #takes the postal code
    lookfor = address_string if postal != "###" else address_string[:-3] # note that '###' means that there is no postal code

    url = f"https://api.mapbox.com/search/geocode/v6/forward?q={lookfor}.json"

    response = requests.get(url, params=payload)
    print(response.status_code) #code 200 means that the geocoder is working
    data = json.loads(response.text)
    # print(json.dumps(data, indent=2))

    if 'features' not in data:
        return None

    else:
        try:

            #edge case: if there are no features
            if len(data['features']) == 0:
                return None

            if len(data['features']) > 0:
                exact_match = False #flag
                if postal != '###': # if there is a postal code
                    for feature in data['features']:
                        try:
                            if not feature['properties']['context']: break #edge case: if there's no postalcode returned in the JSON object
                            if postal in feature['properties']['context']['postcode']['name']: #if the substring is in the postcode
                                exact_match = True
                                # in the form Point(lat, long)
                                coord = Point(feature['geometry']['coordinates'][0],
                                              feature['geometry']['coordinates'][1])
                                break
                        except KeyError:
                            pass

                # if you didn't find an exact match just choose the first or the postal is ###
                if not exact_match:
                    first_result = data['features'][0]
                    coord = Point(first_result['geometry']['coordinates'][0],
                                  first_result['geometry']['coordinates'][1])

                return coord

        except(UnboundLocalError, KeyError):
            pass

    return None  # data


#example
#print(geocode("121 DUNDAS ST WM5G"))
