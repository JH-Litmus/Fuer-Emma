import math
import sys

def divisors(n):
    divs = [1]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
        divs.extend([n])
    return list(set(divs))

while 1==1:
    try:
        a,b,c,d = map(int, input("type in 4 numbers from upper row to lower row with space.\nPress ENTER if quit:").split( ))
        print('')
    except:
        print("\nBye, Emma!")
        sys.exit()
    else:
        div_a = divisors(min(a,c))
        div_b = divisors(min(b,d))
        div_c = divisors(min(a,b))
        div_d = divisors(min(c,d))

        i = 1
        for j in div_a:
            j = int(j)
            for k in div_b:
                k = int(k)
                for l in div_c:
                    l = int(l)
                    for m in div_d:
                        m = int(m)
                        if (j*l==a and k*l==b) and (j*m==c and k*m==d):
                            j = int(j)
                            print(str(i)+") "+str(j)+', '+str(k)+', '+str(l)+', '+str(m))
                            i += 1
        if i==1: print('none\n')
        print('\n')
        
