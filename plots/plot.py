import json

from active_ip import active_ip


DATA_PATH = "./plots/stats.json"
OUTPUT_PATH = "./plots/"

with open(DATA_PATH, "r") as f:
    data = json.loads(f.read())
    active_ip(data, OUTPUT_PATH + "active_ip.png")
