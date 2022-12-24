#!/bin/bash

for i in {0..15}
do
nohup python ./nmap_scan.py -i target_ip.txt -o nmap_result -p $i -t 16 > ./logs/nmap_scan_$i.log &
done