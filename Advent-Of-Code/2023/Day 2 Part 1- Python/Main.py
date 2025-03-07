#2006
n=0
h=open("Advent-of-Code/2023/Python/Day 2 Part 1- Python/Input.txt",'r')  
for i in h.readlines():
    l=i
    z=0
    I,H=l.split(":")
    H = H.split(";")
    for K in H:
        V=K.split(',')
        for c in V:
            Q,J=c.split()
            if int(Q)>12 and J=="red":z+=1
            elif int(Q)>13 and J=="green":z+=1
            elif int(Q)>14 and J=="blue":z+=1
    if z==0:
        I=I.split()[1]
        I=int(I)
        n+=I 
print(n)
