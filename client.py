import requests
import json
data = requests.post('http://127.0.0.1:5000/todos', json={"task": "value dasd asdas"})
data_json = data.json()
print(data_json['task'])
