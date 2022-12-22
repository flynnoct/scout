# Run Scan

```shell
sudo masscan -c masscan.conf
python extract_ip.py -i masscan-output.json -o target_ip.txt
bash launch_nmap_scan.sh
```