import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser(description='Store key-value pair and retrieve it')

parser.add_argument('--key', nargs='?',
                    help='the key of key-value pair to be stored')

parser.add_argument('--value', nargs='+',
                    help='the value of key-value pair to be stored')

args = parser.parse_args()
key_pair_object = vars(args)

with open("test.txt", "r") as f:
    content = f.read()

    try:
        if not content:
            storage = {}
        else:
            storage = json.loads(content)

        # if value exists within incoming parameters then need
        # to write such value by given key
        if key_pair_object['value']:
            if key_pair_object['key']:
                if not key_pair_object['key'] in storage:
                    storage[key_pair_object['key']] = []
                for i in key_pair_object['value']:
                    storage[key_pair_object['key']].append(i)

            with open("test.txt", "w") as f_write:
                f_write.write(json.dumps(storage))

            print("new value added")
        else:
            if key_pair_object['key'] in storage:
                [print(x) for x in storage[key_pair_object['key']]]
            else:
                print("no values found for the key: ", key_pair_object['key'])

    except ValueError as e:
        print("Error occurs", e)

