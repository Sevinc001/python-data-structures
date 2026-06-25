# ==========================================
# TASK 1: Read file and print in UPPER CASE
# ==========================================
fname = input("Enter file name: ")
fhand = open(fname)
text = fhand.read()
A = text.upper()
A = A.rstrip()
print(A)

# ==========================================
# TASK 2: Simple Log Error Finder
# ==========================================
fname2 = input("Enter file name:")
fh2 = open(fname2)
count = 0
for line in fh2:
    if not line.startswith("[ERROR]"):
        continue
    pos = line.find(":")
    A = line[pos - 2 : pos + 6]
    X = A.strip()
    print(X)
    count = count + 1
print("Cəmi xəta sayı:", count)
