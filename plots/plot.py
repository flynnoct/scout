import json

from active_ip import active_ip
from port_dist import port_dist
from cve_port_dist import cve_port_dist
from cve_ip_dist import cve_ip_dist
from key_cve_from_vulscan import key_cve_from_vulscan
from different_cve import different_cve



DATA_PATH = "./plots/stats.json"
OUTPUT_PATH = "./plots/"

with open(DATA_PATH, "r") as f:
    data = json.loads(f.read())
    # active_ip(data, OUTPUT_PATH + "active_ip.png")
    # port_dist(data, OUTPUT_PATH + "port_dist.png")
    # cve_port_dist(data, OUTPUT_PATH + "cve_port_dist.png")
    # cve_ip_dist(data, OUTPUT_PATH + "cve_ip_dist.png")
    # key_cve(data, OUTPUT_PATH + "key_cve.png")
    different_cve(data)
