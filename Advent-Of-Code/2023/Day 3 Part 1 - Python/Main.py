h=open("Advent-of-Code/2023/Python/Day 3 Part 1 - Python/Inputs.txt",'r') 
symbol = ["*","%","/","#","=","+","_","@","-","$"]
temp = 0
for i in h.readlines():
    for x in i:
        if x in symbol:
            if i[x-1] == ".":
                pass
            else:
                z = False
                i = 0
                while z != True:
                    if len(x)-i == ".":
                        for i in range (len(x) - len((x-i))):

                    
            