f = open('inputFile.txt', 'r')
count = 0
# Creates a new file that writes all the people that passed 
passFile = open('PassFile.txt', 'w')
failFile = open('FailFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    # print(str(count)," ", line)
    # count+=1
    # print(f.read())
    else:
        failFile.write(line)
f.close()
passFile.close()
failFile.close()

