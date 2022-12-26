import matplotlib.pyplot as plt
import numpy as np

IP_PREFIX = ["166.111", "59.66", "183.172", "183.173", "101.5", "101.6", "118.229"]

def port_dist(data, output_path):
    x_labels = ["166.111.0.0/16", "59.66.0.0/16", "183.172.0.0/16", "183.173.0.0/16", "101.5.0.0/16", "101.6.0.0/16", "118.229.0.0/19"]
    x = np.arange(len(x_labels))
    # y1 = [5000, 5000, 5000, 5000, 5000, 5000, 5000]
    # y2 = [3000, 3000, 3000, 3000, 3000, 3000, 3000]
    # y3 = [2000, 2000, 2000, 2000, 2000, 2000, 2000]

    stats = {}
    for ip in data:
        prefix = ip.split(".")[0] + "." + ip.split(".")[1]
        if prefix not in stats:
            stats[prefix] = {}
        for port in data[ip]:
            if port not in stats[prefix]:
                stats[prefix][port] = 0
            stats[prefix][port] += 1

    y1 = []
    y1_label = []
    y2 = []
    y2_label = []
    y3 = []
    y3_label = []

    for prefix in IP_PREFIX:
        if prefix not in stats:
            y1.append(0)
            y1_label.append("")
            y2.append(0)
            y2_label.append("")
            y3.append(0)
            y3_label.append("")
            continue
        sorted_ports = sorted(stats[prefix], key=lambda x: stats[prefix][x], reverse=True)
        y1.append(stats[prefix][sorted_ports[0]])
        y1_label.append(sorted_ports[0])
        y2.append(stats[prefix][sorted_ports[1]])
        y2_label.append(sorted_ports[1])
        y3.append(stats[prefix][sorted_ports[2]])
        y3_label.append(sorted_ports[2])


    plt.figure(1, dpi=300)
    plt.title("Top 3 Ports in Each IP Prefix (2022-12)")
    ax = plt.subplot(1, 1, 1)

    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.grid(ls = "--", lw=0.5, color="#4E616C", axis="y")
    ax.xaxis.set_tick_params(rotation=30)
    ax.set_ylabel("Number of Open Ports")
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)

    width = 0.3

    ax.bar(x - width, y1, width, bottom=0, color="#00A752", label="Top 1")
    ax.bar(x, y2, width, bottom=0, color="#00579C", label="Top 2")
    ax.bar(x + width, y3, width, bottom=0, color="#FFC107", label="Top 3")

    ax.legend(loc="upper right")

    print("##### Top 1 #####")
    print(y1_label)
    print(y1)
    print("##### Top 2 #####")
    print(y2_label)
    print(y2)
    print("##### Top 3 #####")
    print(y3_label)
    print(y3)

    # Add data text
    # for a, b, c in zip(x, y1, y1_label):
    #     ax.text(a, b, b, ha='center', va='bottom', fontsize=8)
    #     ax.text(a, b, c, ha='center', va='top', fontsize=8)
    
    # for a, b, c in zip(x_labels, y2, y2_label):
    #     ax.text(a, b, b, ha='center', va='bottom', fontsize=8)
    #     ax.text(a, b, c, ha='center', va='top', fontsize=8)

    # for a, b, c in zip(x_labels, y3, y3_label):
    #     ax.text(a, b, b, ha='center', va='bottom', fontsize=8)
    #     ax.text(a, b, c, ha='center', va='top', fontsize=8)

    plt.savefig(output_path, dpi=300, bbox_inches='tight')