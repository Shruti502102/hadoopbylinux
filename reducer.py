import sys
from collections import defaultdict

current_key = None
a_values = defaultdict(float)
b_values = defaultdict(float)

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    
    if current_key != key:
        if current_key is not None:
            total = 0
            for idx in a_values:
                total += a_values[idx] * b_values.get(idx, 0)
            print(f"{current_key}\t{total}")
        current_key = key
        a_values = defaultdict(float)
        b_values = defaultdict(float)

    tag, idx, val = value.split(',')
    if tag == 'A':
        a_values[idx] = float(val)
    else:
        b_values[idx] = float(val)

# Final output for last key
if current_key:
    total = 0
    for idx in a_values:
        total += a_values[idx] * b_values.get(idx, 0)
    print(f"{current_key}\t{total}")
