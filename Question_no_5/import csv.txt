import csv
import requests
from pathlib import Path

url = "https://reqres.in/api/users?page=1"
headers = ["id", "email", "first_name", "last_name", "avatar"]

with open("users.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    
    for page in range(1, 3):
        response = requests.get(url.format(page=page))
        data = response.json()
        
        for user in data["data"]:
            row = [user["id"], user["email"], user["first_name"], user["last_name"], user["avatar"]]
            writer.writerow(row)
