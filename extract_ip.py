import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="Input File", type=str)
parser.add_argument("-o", "--output", help="Output File", type=str)

args = parser.parse_args()

with open(args.input, "r") as f:
    masscan_data = json.load(f)

deduplicate_data = set()

for item in masscan_data:
    deduplicate_data.add(item["ip"])

with open(args.output, "w") as wf:
    for ip in deduplicate_data:    
        wf.write(ip + "\n")

