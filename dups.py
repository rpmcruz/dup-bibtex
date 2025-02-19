import argparse
parser = argparse.ArgumentParser()
parser.add_argument('input', nargs='+')
args = parser.parse_args()

import re

d = {}

for file in args.input:
    for line in open(file):
        match = re.search(r'@\w+\{([^,]+),', line)
        if match:
          entry = match.group(1)
        match = re.search(r'^\s*title\s*=\s*["]?\s*\{(.+)\}\s*["]?\s*,', line)
        if match:
            title = match.group(1)
            d[entry] = title.lower()

import difflib
count = 0
already_matched = []
for e1, t1 in d.items():
    for e2, t2 in d.items():
        if e1 != e2 and e2 not in already_matched:
            similarity = difflib.SequenceMatcher(None, t1, t2)
            if similarity.ratio() > 0.9:
                print('very similar')
                print(e1, t1)
                print(e2, t2)
                print()
                count += 1
    already_matched.append(e1)
print('duplicates are', count)
