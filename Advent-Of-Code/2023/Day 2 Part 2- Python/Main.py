#84911
n=0
h=open("Advent-of-Code/2023/Python/Day 2 Part 2- Python/Input.txt",'r')  
total = 0
for i in h.readlines():
    l=i
    red = 0
    green = 0
    blue = 0
    I,H=l.split(":")
    H = H.split(";")
    for K in H:
        V=K.split(',')
        for c in V:
            Q,J=c.split()
            if int(Q)>red and J=="red":
                red = int(Q)
            elif int(Q)>green and J=="green":
                green = int(Q)
            elif int(Q)>blue and J=="blue":
                blue = int(Q)
    total += (green*blue*red)
print(total)
