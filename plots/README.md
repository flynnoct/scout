# Plots

## Pipeline

1. Transform nmap resule data into a statistic format that can be plotted.
2. Plot the data.

## What to Plot

- 各个网段、总体的在线数量；
- 各个网段、总体操作系统的分布 (Windows, Linux, macOS, iOS, Android);
- 各个网段、总体的服务分布（端口）;
- 各个端口的平均漏洞数量（5%-95%箱线图，选一个数据库）；
- 各个网段、总体平均漏洞数量（5%-95%箱线图，选一个数据库）；
- 选几个有代表性的CVE漏洞，查看其总体分布情况；
    1. [WannaCry (CVE-2017-0144)](https://nmap.org/nsedoc/scripts/smb-vuln-ms17-010.html)
    2. [Heartbleed (CVE-2014-0160)](https://nmap.org/nsedoc/scripts/ssl-heartbleed.html)
    3. [ShellShock (CVE-2014-6271, CVE-2014-7169)](https://nmap.org/nsedoc/scripts/http-shellshock.html)
    4. SambaCry (CVE-2017-7494)
    5. Badlock (CVE-2016-2118)
    6. POODLE (CVE-2014-3566)
    7. Venom (CVE-2015-3456)
    8. Windows Sandworm (CVE-2014-4114)
    9. [Log4J (CVE-2021-44228, CVE-2021-45046)](https://github.com/giterlizzi/nmap-log4shell)
    10. Atlassian Confluence RCE (CVE-2022-26134)
