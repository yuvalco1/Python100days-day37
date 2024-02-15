import json
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# .env file contains api keys in the format of API_KEY="xxxxxx", get it using os.environ['API_KEY']
load_dotenv()  # take environment variables from .env.


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "yuvalco1"

pixela_parameters = {
    "token": os.environ['PIXELA_API_TOKEN'],
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# this code will create a new user in the pixela server, run once and was successful
# response = requests.post(url=PIXELA_ENDPOINT, json=pixela_parameters)
# print(response.text)

# this code will create a new graph in the pixela server, run once and was successful
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_parameters = {
    "username": USERNAME,
    "id": "python-graph",
    "name": "Python 100 Days graph, how much 'days' did I learn?",
    "unit": "days",
    "type": "int",
    "color": "shibafu",
    "timezone": "Africa/Cairo",
}

headers = {
    "X-USER-TOKEN": os.environ['PIXELA_API_TOKEN']

}
# Graph creation, done once
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

# code for posting data to update the graph, run every day
graph_add_data_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/python-graph"

today = datetime.today().strftime("%Y%m%d")
print(today)

add_data_parmaters = {
    "date": today,
    "quantity": "2",
    "optionalData": json.dumps("day37"),
}
# response = requests.post(url=graph_add_data_endpoint, json=add_data_parmaters, headers=headers)
# print(response.text)
#
#
graph_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/python-graph/{today}"
update_parameters = {
    "quantity": "1"
}

response2 = requests.post(url=graph_update_endpoint, json=update_parameters, headers=headers)
print(response2.text)