import requests
import connect

# https://pixe.la/v1/users/ziffic/graphs/graph1.html
USER_NAME = "ziffic"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

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
    "id": "graph1",
    "name": "Dr Pepper Graph",
    "unit": "bottles",
    "type": "float",
    "color": "sora"
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=connect.headers)
print(response.text)

