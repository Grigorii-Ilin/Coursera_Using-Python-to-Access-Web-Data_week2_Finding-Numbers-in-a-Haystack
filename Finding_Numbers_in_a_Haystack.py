import re

hand=open('regex_sum_85333.txt')
Summ=0

for line in hand:
    line=line.rstrip()       
    NumbersInLine=re.findall('[0-9]+', line)

    for Num in NumbersInLine:
        Summ+=int(Num)

print(Summ)

    

    