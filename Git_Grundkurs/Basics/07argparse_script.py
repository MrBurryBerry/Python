#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Test zum üben von argparse in Python.')
parser.add_argument("pflicht_int", help="Integer ist erforderlich", type=int)
parser.add_argument("--optional_int", help="Optionaler Integer", type=int)
args = parser.parse_args()

print("Integer:", args.pflicht_int, "- Typ:", type(args.pflicht_int))
print("Optionaler Integer:", args.optional_int)
print('ende')
