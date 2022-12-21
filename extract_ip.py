import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="Input File", type=str)
parser.add_argument("-o", "--output", help="Output File", type=str)

args = parser.parse_args()

with open(args.input, "r") as f:
    