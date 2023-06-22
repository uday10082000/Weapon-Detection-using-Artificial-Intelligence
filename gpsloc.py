import requests
import json
def get_loc():
    send_url = "http://api.ipstack.com/check?access_key=d22988a44bcf41c239a4e3a799df6b45"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']
    loc=str(latitude)+","+str(longitude)
    city=str(city)
    return city
#print("location==",get_loc())
