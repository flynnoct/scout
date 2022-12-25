#!/bin/bash

for i in {0..7}
do
nohup python ./nmap_scan.py -i target_ip.txt -o nmap_result -p $i -t 8 > ./logs/nmap_scan_$i.log &
done