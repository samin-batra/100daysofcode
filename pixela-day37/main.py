import requests
import datetime

url = "https://pixe.la/v1/users"

data = {
    "token":"myTokenSem",
    "username": "saminbatra",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# res = requests.post(url = url, json = data)
# # res.raise_for_status()
# print(res.status_code)
# print(res.json())

USER_NAME = "saminbatra"
GRAPH_ID = "mygraph1"

#Create the graph
graph_url = f"https://pixe.la/v1/users/{USER_NAME}/graphs"

header = {
    "X-USER-TOKEN": "myTokenSem"
}

params = {
    "id": "mygraph1",
    "name": "runner-tracker",
    "unit": "kilometer",
    "type": "float",
    "color": "shibafu"
}

# graph_res = requests.post(url = graph_url, json = params, headers = header)
# print(graph_res.json())


#Post a pixel to the graph
pixel_post = f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}"
curr_date = datetime.datetime.now()
formatted_date = curr_date.strftime("%Y%m%d")
print(formatted_date)
params = {
    "date": formatted_date,
    "quantity": "2.5"
}

res = requests.post(url = pixel_post, json = params, headers = header)
print(res.text)