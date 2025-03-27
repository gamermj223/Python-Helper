import json

json_string = '{"name": "Mark", "age": "16"}'

data = json.loads(json_string)
print(data["name"])
