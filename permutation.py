'''from itertools import permutations
Z = input().split()
A = "".join(Z[0])
A2 = "".join(Z[1])
A2 = int(A2)
A = ''.join(sorted(A))
B = (list(permutations(A,A2)))
newB = [list(x) for x in B]
len1 = len(newB)
for u in range(0,len1):
    e = newB[u]
    print("".join(e))


from itertools import permutations
Z = input().split()
A = "".join(sorted(Z[0]))
A2 = int("".join(Z[1]))
B = [list(x) for x in (list(permutations(A,A2)))]
for u in range(0,len(B)):
    print("".join(B[u]))
'''

from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
