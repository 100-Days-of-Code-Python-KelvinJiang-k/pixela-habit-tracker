import requests
from datetime import datetime
import os

# Project link: https://pixe.la/v1/users/kelvinj/graphs/graph1.html

PIXELA_TOKEN = os.environ.get("PIXELA_API_KEY")
USERNAME = "kelvinj"
# for greater security compared to params
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

pixela_endpoint = "https://pixe.la/v1/users"
user_config = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Created Pixela user account:
# response = requests.post(url=pixela_endpoint, json=user_config)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}

# Created Pixela graph definition:
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


def graph_pixel(date: str, quantity: str):
    update_params = {
        "date": date,
        "quantity": quantity,
    }
    update_endpoint = f"{graph_endpoint}/{graph_config['id']}"
    response = requests.post(url=update_endpoint, json=update_params, headers=headers)
    print(response.text)


km_biked = "8"
current_date = datetime(year=2022, month=8, day=28).strftime("%Y%m%d")
graph_pixel(current_date, km_biked)

