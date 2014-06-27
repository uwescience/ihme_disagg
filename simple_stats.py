#!/usr/bin/env python

import csv
import random
import sys

from collections import Counter

phile = sys.argv[1]

categories = Counter()
num_labels = Counter()

NUM_CATEGORIES = 6

with open(phile, 'rb') as fh:
    reader = csv.reader(fh)
    it = iter(reader)
    header = next(it)
    labels = header[-1 * NUM_CATEGORIES:]
    print labels

    for row in it:
        vals = [int(x) for x in row[-1 * NUM_CATEGORIES:]]
        nl = sum(vals)
        num_labels[nl] += 1

        for label, val in zip(labels, vals):
            categories[label] += val

    print categories
    print sum(categories.values())
    print
    print num_labels
    print sum(num_labels.values())
