counter = 0

def isAnagram(word1, word2):
    if len(word1) == len(word2):
        for letter in word1:
            word2 = word2.replace(letter, '')
    if len(word2) == 0:
        return True
    else:
        return False

def parseLine(line):
    for i in range(len(line) - 1):    
        for j in range (i + 1, len(line)):
            if (line[i] == line[j] or isAnagram(line[i], line[j])):
                return 0
    return 1

with open('4-1.in') as f:
    for line in f:
        line = line.split()
        counter += parseLine(line)

print(counter)