import matplotlib.pyplot as plt

IP_PREFIX = ["166.111", "59.66", "183.172", "183.173", "101.5", "101.6", "118.229"]

def cve_port_dist(data, output_path):
    stats = {}
    count = {}

    for ip in data:
        for port in data[ip]:
            if port not in stats:
                stats[port] = 0
                count[port] = 0
            stats[port] += len(data[ip][port]["CVE"])
            count[port] += 1
    
    sorted_ports = sorted(count, key=lambda x: count[x], reverse=True)
    x = sorted_ports[:10]
    y = [stats[port] / count[port] for port in x]
    
    plt.figure(1, dpi=300)
    plt.title("Top 10 Open Ports with CVEs (2022-12)")
    ax = plt.subplot(1, 1, 1)

    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.grid(ls = "--", lw=0.5, color="#4E616C", axis="y")
    ax.xaxis.set_tick_params(rotation=30)
    
    ax.set_ylabel("Average Number of CVEs")

    ax.bar(x, y, color="#B22222")

    for a, b in zip(x, y):
        ax.text(a, b, "%.0f" % b, ha='center', va='bottom', fontsize=8)

    
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
