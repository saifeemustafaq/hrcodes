#Given the participants' score sheet for your University Sports Day, 
#you are required to find the runner-up score. 
#You are given scores. Store them in a list and find the score of the runner-up. 

def dupl(A):
    newlist=[]
    for num in A:
        if num not in newlist:
            newlist.append(num)
    return newlist

n = int(input())
A = [int(x) for x in input().split()]
newA = sorted((dupl(A)))
print(newA[len(newA)-2])
