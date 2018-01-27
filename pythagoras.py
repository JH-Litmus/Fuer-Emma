
import math
import sys

def divisors(n):
    divs = [1]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
        divs.extend([n])
    return list(set(divs))

# for j in a:
#     if divisors(j) == [1,j]:
#         b.append(j)

for j in range(1,100):
    for k in range(j+1,100):
        for l in range(k+1,100):
            if j**2 + k**2 == l**2: print(j, k, l, 'yes', sep=', ')
