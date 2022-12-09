
file1 = open('onelinefile.txt', 'r')

file2 = open('Filename2.csv','w')

content = file1.read()

content = content.split()

for i in range(0, len(content), 4):
    file2.write(content[i] + ',' + content[i+1] + ',' + content[i+2] + ',' + content[i+3] + '\n')

file1.close()
file2.close()