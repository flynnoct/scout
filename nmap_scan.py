import argparse
import os
from tqdm import tqdm
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="Input Target IP File", type=str)
parser.add_argument("-o", "--output", help="Output Directory", type=str)
parser.add_argument("-p", "--process", help="Process ID", type=int)
parser.add_argument("-t", "--total", help="Total Process Number", type=int)

args = parser.parse_args()

ip_list = []
with open(args.input, "r") as f:
    ip_list = f.readlines()
ip_list = list(map(lambda x: x.strip(), ip_list))

start_time = datetime.datetime.now()
print("Start time: %s" % start_time.strftime("%Y-%m-%d, %H:%M:%S"))

for ip in tqdm(ip_list):
    if (ip_list.index(ip) % args.total) == args.process:
        cmd = "nmap -sV -Pn --script=vulscan/vulscan.nse %s > ./%s/%s.txt" % (ip, args.output, ip)
        os.system(cmd)

end_time = datetime.datetime.now()
print("Start time: %s" % end_time.strftime("%Y-%m-%d, %H:%M:%S"))
duration = end_time - start_time
print("Duration: %ss" % str(duration.seconds))