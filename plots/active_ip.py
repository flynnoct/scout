import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

IP_PREFIX = ["166.111", "59.66", "183.172", "183.173", "101.5", "101.6", "118.229"]
TOTAL = [65536, 65536, 65536, 65536, 65536, 65536, 8192]

def active_ip(data, output_path):
    x = ["166.111.0.0/16", "59.66.0.0/16", "183.172.0.0/16", "183.173.0.0/16", "101.5.0.0/16", "101.6.0.0/16", "118.229.0.0/19"]

    y1 = [len([ip for ip in data.keys() if ip.startswith(ip_prefix)]) for ip_prefix in IP_PREFIX]

    y2 = [y1[i] / TOTAL[i] for i in range(len(y1))]

    plt.figure(1, dpi=300)
    plt.title("Active Hosts in Each IP Prefix (2022-12)")
    ax1 = plt.subplot(1, 1, 1)

    ax1.spines["left"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    ax1.grid(ls = "--", lw=0.5, color="#4E616C", axis="y")
    ax1.xaxis.set_tick_params(rotation=30)
    ax1.set_ylabel("Number of Active Hosts")

    ax1.set_ylim(0, 8000)
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(2000))

    ax1.bar(x, y1, color="#FFA500")

    for a, b in zip(x, y1):
        ax1.text(a, b + 300, b, ha='center', va='center', fontsize=8)

    # plot percentage on ax2
    ax2 = ax1.twinx()
    ax2.spines["left"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_ylim(0, 1)
    ax2.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=0))
    ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.25))
    ax2.set_ylabel("Percentage of Active Hosts")

    ax2.plot(x, y2, color="#00A752", marker="o", markersize=5, linewidth=2)

    for a, b in zip(x, y2):
        ax2.text(a, b, "%.2f%%" % (b * 100), ha='center', va='bottom', fontsize=8)

    plt.savefig(output_path, dpi=300, bbox_inches='tight')