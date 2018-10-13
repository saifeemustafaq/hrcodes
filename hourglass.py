A1 = [int(x) for x in input().split()]
A2 = [int(x) for x in input().split()]
A3 = [int(x) for x in input().split()]
A4 = [int(x) for x in input().split()]
A5 = [int(x) for x in input().split()]
A6 = [int(x) for x in input().split()]

A = [A1,A2,A3,A4,A5,A6]

for i in range(0,4):
    if i<7:
        a = A1[i]+A1[i+1]+A1[i+2]
        print(a)
        if i<7:
            b = A2[i]
