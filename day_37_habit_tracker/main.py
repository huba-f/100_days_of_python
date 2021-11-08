import requests
from datetime import datetime

TOKEN = "kfglendvyusehvpqjch"
USERNAME = "huba"
GRAPH_ID = "graph3"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Time spent learning",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": str(input("How many hours did you code today: "))
}
### ADD NEW ###

response = requests.update(url=pixel_endpoint, json=pixel_data, headers=headers)

print(response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# new_pixel_data = {
#     "quantity": "2.30"
# }
#

### UPDATE OLD ###

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#
# print(response.text)