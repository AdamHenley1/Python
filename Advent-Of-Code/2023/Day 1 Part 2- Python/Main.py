#54530
h = open("Advent-of-Code/2023/Python/Day 1 Part 2- Python/Inputs.txt",'r')  
c = 0
for z in h.readlines():
    t=0
    l=0
    p=z
    p=p.replace("one","o1e")
    p=p.replace("two","t2o")
    p=p.replace("three","t3e")
    p=p.replace("four","f4r")
    p=p.replace("five","f5e")
    p=p.replace("six","s6x")
    p=p.replace("seven","s7n")
    p=p.replace("eight","e8t")
    p=p.replace("nine","n9e")
    for e in p:
        if e.isdigit()==True:
            if t==0:
                f=e
                t+=1
            elif t>=1:l=e
    if l==0:l=f
    g=str(f)+str(l)
    c+=int(g)
print(c)