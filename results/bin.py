import collections

counter = collections.Counter()
with open('OUTPUT.txt') as fh:
    for line in fh:
        tok = line.split(',')[-1].strip()
        counter[tok] += 1

print counter
print sum(counter.values())
