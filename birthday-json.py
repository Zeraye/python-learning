import json

with open("birthday-json.json", "r") as file:
    info = json.load(file)

if info["has_a_dog"]:
    print("{} has a dog".format(info["name"]))
else:
    print("{} does not have a dog".format(info["name"]))
