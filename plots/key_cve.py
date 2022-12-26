import os
import matplotlib.pyplot as plt
import numpy as np

def get_vul_list(dir):
    vul_list = []
    for file in os.listdir(dir):
        if file.endswith(".txt"):
            with open(dir + "/" + file, "r") as f:
                data = f.readlines()
                data = list(map(lambda x: x.strip(), data))
                for line in data:
                    if "VULNERABLE" in line:
                        vul_list.append(file.replace(".txt", ""))
                        break
    return vul_list

vul_lists = {}

vul_lists["ms17-010"] = get_vul_list("./nmap_result_ms17")
vul_lists["heartbleed"] = get_vul_list("./nmap_result_heartbleed")

stats = {}

for vul in vul_lists:
    stats[vul] = {}
    for ip in vul_lists[vul]:
        ip_prefix = ip.split(".")[0] + "." + ip.split(".")[1]
        if ip_prefix not in stats[vul]:
            stats[vul][ip_prefix] = 0
        stats[vul][ip_prefix] += 1

x_labels = ["166.111.0.0/16", "59.66.0.0/16", "183.172.0.0/16", "183.173.0.0/16", "101.5.0.0/16", "101.6.0.0/16", "118.229.0.0/19"]
x = np.arange(len(x_labels))

y1 = []
for prefix in x_labels:
    prefix = prefix.split(".")[0] + "." + prefix.split(".")[1]
    if prefix not in stats["ms17-010"]:
        y1.append(0)
    else:
        y1.append(stats["ms17-010"][prefix])

y2 = []
for prefix in x_labels:
    prefix = prefix.split(".")[0] + "." + prefix.split(".")[1]
    if prefix not in stats["heartbleed"]:
        y2.append(0)
    else:
        y2.append(stats["heartbleed"][prefix])

plt.figure(1, dpi=300)
plt.title("Number of EternalBlue & Heartbleed Vulnerable Hosts in Each IP Prefix (2022-12)")
ax = plt.subplot(1, 1, 1)

ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.grid(ls = "--", lw=0.5, color="#4E616C", axis="y")
ax.xaxis.set_tick_params(rotation=30)

ax.set_ylabel("Number of Hosts")

width = 0.3

ax.bar(x - width / 2, y1, width, color="#B22222", label="EternalBlue")
ax.bar(x + width / 2, y2, width,  color="#FFA500", label="Heartbleed")

ax.legend()

ax.set_xticks(x)
ax.set_xticklabels(x_labels)

for a, b in zip(x, y1):
    ax.text(a - width / 2, b, "%d" % b, ha='center', va='bottom', fontsize=8)

for a, b in zip(x, y2):
    ax.text(a + width / 2, b, "%d" % b, ha='center', va='bottom', fontsize=8)

plt.savefig("./plots/key_cve.png", dpi=300, bbox_inches="tight")
