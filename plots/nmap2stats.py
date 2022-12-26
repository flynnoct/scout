import os
import re
import json
from tqdm import tqdm

DATA_DIR = "./nmap_result/"

data = {}

for filename in tqdm(os.listdir(DATA_DIR)):
    if filename.endswith(".txt"):
        ip = filename.replace(".txt", "")
        with open(DATA_DIR + filename, "r") as f:
            for line in f.readlines():
                if re.match(r"\d+/\w+", line) and "open" in line:
                    port, protocol = line.split(" ")[0].split("/")
                    port_prot = "%s-%s" % (port, protocol)
                    data[ip] = {port_prot: {"CVE": []}}
                if line.startswith("| [CVE-"):
                    data[ip][port_prot]["CVE"].append(line.split(" ")[1].strip("[]"))

with open("./plots/stats.json", "w") as f:
    f.write(json.dumps(data, indent=4))