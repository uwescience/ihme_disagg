#!/usr/bin/env python

import csv
import random
import sys

from collections import Counter

phile = sys.argv[1]

NUM_CATEGORIES = 6
OUTPUT_FILE = 'OUTPUT.txt'

def get_labels(row):
    return [int(x) for x in row[-1 * NUM_CATEGORIES:]]

with open(phile, 'rb') as fh:
    reader = csv.reader(fh)
    it = iter(reader)
    header = next(it)
    all_rows = [row for row in it if sum(get_labels(row)) == 0]
    random.shuffle(all_rows)

valid_responses = set(header[-1 * NUM_CATEGORIES:] + ['X'])
print valid_responses
outputs = []

try:
    for row in all_rows:
        while True:
            ch = raw_input("%s: " % ','.join(row))
            if ch in valid_responses:
                outputs.append(row + [ch])
                break
            else:
                print 'Invalid response'
finally:
    with open(OUTPUT_FILE, 'w') as fh:
        for output in outputs:
            fh.write(','.join(output) + '\n')
