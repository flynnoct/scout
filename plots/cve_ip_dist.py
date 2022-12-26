import matplotlib.pyplot as plt

IP_PREFIX = ["166.111", "59.66", "183.172", "183.173", "101.5", "101.6", "118.229"]

def cve_ip_dist(data, output_path):

    x = ["166.111.0.0/16", "59.66.0.0/16", "183.172.0.0/16", "183.173.0.0/16", "101.5.0.0/16", "101.6.0.0/16", "118.229.0.0/19"]
    stats = {}
    count = {}

    for ip_prefix in IP_PREFIX:
        stats[ip_prefix] = 0
        count[ip_prefix] = 0

    for ip in data:
        prefix = ip.split(".")[0] + "." + ip.split(".")[1]
        for port in data[ip]:
            stats[prefix] += len(data[ip][port]["CVE"])
        count[prefix] += 1

    y = [stats[prefix] / count[prefix] for prefix in IP_PREFIX]

    ax = plt.subplot(1, 1, 1)

    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)


    ax.bar(x, y, color="#3CB371")

    ax.set_title("CVEs in Each IP Prefix (2022-12)")
    ax.set_ylabel("Average Number of CVEs per IP")

    ax.grid(ls = "--", lw=0.5, color="#4E616C", axis="y")
    ax.xaxis.set_tick_params(rotation=30)

    for a, b in zip(x, y):
        ax.text(a, b, "%.0f" % b, ha='center', va='bottom', fontsize=8)
        
    plt.savefig(output_path, dpi=300, bbox_inches="tight")