def different_cve(data):
    stats = {}
    stats["all"] = set()
    for ip in data:
        ip_prefix = ip.split(".")[0] + "." + ip.split(".")[1]
        if ip_prefix not in stats:
            stats[ip_prefix] = set()
        for port in data[ip]:
            for cve in data[ip][port]["CVE"]:
                stats[ip_prefix].add(cve)
                stats["all"].add(cve)
    for ip_prefix in stats:
        print(ip_prefix, len(stats[ip_prefix]))

