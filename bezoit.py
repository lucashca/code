

import sys

param = sys.argv[1:] 
a = int(param[0],10)
b = int(param[1],10)      
t = []
s = []
r = []
q = []
s.append(1)
s.append(0)
t.append(0)
t.append(1)
q.append(None)
q.append(None)



def bezoit(a,b,i):
    global r,s,t,q
    ra = b
    qi = a//b
    ri = a%b
    si = s[i-2] - qi*s[i-1]
    ti = t[i-2] - qi*t[i-1]
    t.append(ti)
    s.append(si)
    if ri == 1:
        return (s[i],t[i])
    elif ri == 0:
        return (s[i-1],t[i-1])
    else:
        q.append(qi)
        r.append(ri)
        return bezoit(ra,ri,i+1)
    

r.append(a)
r.append(b)

(x,y) = bezoit(a,b,2)
mmc = a*x + b*y 
print('(',x,',', y,') = bezoit(',a,',',b,');')
print("")
print(mmc," = ",a,'*',x,"+",b,"*",y)
print("")
if mmc == 1: 
    print("MMC = 1. (",a," e ",b,") São primos entre si.")
else:   
    print("MMC = ",mmc,". (",a," e ",b,") Não são primos entre si.")
    