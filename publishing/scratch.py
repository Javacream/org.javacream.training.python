import json

class Demo:
    def __init__(self):
        self.attr = "Hugo"

d = Demo()

demoDict = {
    "attr": "Hugo"
}

demoDict["l"] = ["A", "B", "C"]

print(json.dumps(demoDict))

with open ("demo.json", "wt") as file:
    json.dump(demoDict, file)

with open ("demo.json", "r") as file:
    loaded = json.load(file)
    type(loaded)
    print(loaded.get("attr"))
