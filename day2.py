checksum = 0
with open('inputs/2.in', 'r') as f:
    for line in f:
        line = line.strip("\n").split("\t")
        
        line = [int(l) for l in line]
        row = 0
        for i in range(len(line) - 1):
            for j in range(i + 1, len(line)):
                if line[i] % line[j] == 0:
                    row = line[i] / line[j]
                else:
                    if line[j] % line[i] == 0:
                        row = line[j] / line[i]
        print(row)
        checksum += int(row)

print(checksum)
