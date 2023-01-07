import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv("E:/EnvironmentVariables/.env.txt")

# Enter the number of hours you studied today (as a string) --
quantity = "1.5"

USERNAME = "mudit"
TOKEN = os.getenv("PIXEL_TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# user = requests.post(url=pixela_endpoint, json=user_params)
# print(user.text)

graph_params = {
    "id": "study",
    "name": "Study Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora",
}

authentication = {
    "X-USER-TOKEN": TOKEN,
}
# graph = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs", json=graph_params, headers=authentication)
# print(graph.text)

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity,
}

pixel = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/study", json=pixel_params, headers=authentication)
print(pixel.text)

# delete_pixel = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/study/{today.strftime('%Y%m%d')}",
#                                headers=authentication)
# print(delete_pixel.text)
