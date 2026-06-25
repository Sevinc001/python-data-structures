# ==========================================
# TASK 1: Simple Word Frequency Counter
# ==========================================
text = "Python is fun and python is powerful"
words = text.split()
words_counts = dict()
for word in words:
    words_counts[word] = words_counts.get(word, 0) + 1
print(words_counts)

# ==========================================
# TASK 2: Finding the Most Prolific Sender
# ==========================================
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()
 
for line in fh:
    if line.startswith("From "):
        lyn = line.split()
        email = lyn[1]
        counts[email] = counts.get(email, 0) + 1

maxi_email = None
maxi_count = None
for email, count in counts.items():
    if maxi_count is None or count > maxi_count:
        maxi_count = count
        maxi_email = email
print(maxi_email, maxi_count)
