import requests
import connect

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": connect.PIXELA_TOKEN,
    "username": "ziffic",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

