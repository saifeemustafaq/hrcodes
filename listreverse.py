#reverse given elements
N = int(input())
A = [int(x) for x in input().split()]
B = []
#print(A)

for i in range(N-1,-1,-1):
    B.append(A[i])

print(" ".join(str(x) for x in B))

