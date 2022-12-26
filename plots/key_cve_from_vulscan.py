import matplotlib.pyplot as plt

KEY_CVE = { "CVE-2017-0144": "WannaCry", 
            "CVE-2014-0160": "Heartbleed", 
            "CVE-2014-6271": "Shellshock",
            "CVE-2014-6277": "Shellshock",
            "CVE-2014-6278": "Shellshock",
            "CVE-2014-7169": "Shellshock",
            "CVE-2014-7186": "Shellshock",
            "CVE-2014-7187": "Shellshock",
            "CVE-2017-7494": "SambaCry",
            "CVE-2016-2118": "Badlock",
            "CVE-2014-3566": "POODLE",
            "CVE-2015-3456": "Venom",
            "CVE-2014-4114": "Windows Sandworm",
            "CVE-2021-44228": "Log4J",
            "CVE-2021-45046": "Log4J",
            "CVE-2022-26134": "Atlassian Confluence RCE"
          }

def key_cve_from_vulscan(data, output_path):
    x = [cve for cve in KEY_CVE]
    stats = {cve: 0 for cve in x}
    for ip in data:
        for port in data[ip]:
            for cve in data[ip][port]["CVE"]:
                if cve in stats:
                    stats[cve] += 1
    y = [stats[cve] for cve in x]
    plt.figure(1, dpi=300)
    plt.title("Key CVEs (2022-12)")
    ax = plt.subplot(1, 1, 1)

    ax.spines["left"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.grid(ls = "--", lw=0.5, color="#4E616C", axis="y")
    ax.xaxis.set_tick_params(rotation=30)

    ax.set_ylabel("Number of CVEs")

    ax.bar(x, y, color="#4E616C")

    for a, b in zip(x, y):
        ax.text(a, b, "%.0f" % b, ha='center', va='bottom', fontsize=8)

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    