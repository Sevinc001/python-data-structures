# Description: Parsing a text file, filtering out all duplicate words, and sorting them alphabetically.

fname = input("Enter file name: ")
fh = open(fname)
words = [] 

for line in fh:
    word_list = line.split()
    for word in word_list:
        if word not in words:
            words.append(word)

words.sort()
print(words)
