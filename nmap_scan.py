import argparse
import os
import multiprocessing
from tqdm import tqdm
import datetime

def exec_nmap(ip, dir):
    cmd = "nmap -sV -Pn --script=vulscan/vulscan.nse %s > ./%s/%s.txt" % (ip, dir, ip)
    os.system(cmd)

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="Input Target IP File", type=str)
parser.add_argument("-o", "--output", help="Output Directory", type=str)

args = parser.parse_args()

ip_list = []
with open(args.input, "r") as f:
    ip_list = f.readlines()
ip_list = list(map(lambda x: x.strip(), ip_list))

pool = multiprocessing.Pool(8)

start_time = datetime.datetime.now()
print("Start time: %s" % start_time.strftime("%Y-%m-%d, %H:%M:%S"))

for ip in tqdm(ip_list):
    pool.apply_async(func=exec_nmap, args=(ip, args.output))

pool.close()
pool.join()

end_time = datetime.datetime.now()
print("Start time: %s" % end_time.strftime("%Y-%m-%d, %H:%M:%S"))
duration = end_time - start_time
print("Duration: %ss" % str(duration.seconds))