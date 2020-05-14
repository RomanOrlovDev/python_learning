import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser(description='Store key-value pair and retrieve it')

parser.add_argument('--key', nargs=1,
                    help='the key of key-value pair to be stored')

parser.add_argument('--value', nargs=1,
                    help='the value of key-value pair to be stored')

args = parser.parse_args()
key_pair_object = vars(args)

