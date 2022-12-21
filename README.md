# Run Scan

```shell
sudo masscan -c masscan.conf
python extract_ip.py -i masscan-output.json -o target_ip.txt
python nmap_scan.py -i target_ip.txt -o nmap_result
```