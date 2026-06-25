# Description: Analyzing mail logs to extract timestamps, count hourly frequencies, and sort them chronologically using tuples.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()

for line in fh:
    if line.startswith("From "):
        lyn = line.split()
        times = lyn[5]
        H = times.split(":")
        hour = H[0]
        counts[hour] = counts.get(hour, 0) + 1

houres = sorted(counts.items())
for k, v in houres:
    print(k, v)
