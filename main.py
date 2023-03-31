import requests
import connect
from datetime import datetime

# https://pixe.la/v1/users/ziffic/graphs/graph1.html
USER_NAME = "ziffic"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

user_params = {
    "token": connect.PIXELA_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Dr Pepper Graph",
    "unit": "bottles",
    "type": "float",
    "color": "sora"
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=connect.headers)
# print(response.text)

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Dr. Peppers did you drink today?")
}

response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=connect.headers)
print(response.text)

update_date = datetime(year=2023, month=3, day=29).strftime("%Y%m%d")
put_endpoint = f"{PIXEL_ENDPOINT}/{update_date}"

pixel_update = {
    "quantity": "4.0"
}

# response = requests.put(url=put_endpoint, json=pixel_update, headers=connect.headers)
# print(response.text)

# response = requests.delete(url=put_endpoint, json=pixel_update, headers=connect.headers)
# print(response.text)
