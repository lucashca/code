
import sys
import math
##Testing
param = sys.argv[1:]
mode = param[0]

def set_mode(mode):
    if mode == "-primo":
        a = int(param[1],10)
        primos(a)
    elif mode == "-inverso":
        a = int(param[1],10)
        n = int(param[2],10)
        inverso(a,n)
    elif mode == "-exp_mod":
        a = int(param[1],10)
        x = int(param[2],10)
        n = int(param[3],10)
        exp_mod(a,x,n)
    elif mode == "-exp_oti":
        a = int(param[1],10)
        x = int(param[2],10)
        n = int(param[3],10)
        exp_mod_otimizado(a,x,n)
    elif mode == "--mdce":
        a = int(param[1],10)
        b = int(param[2],10)
        mdce(a,b)
    

def mdce(a,b):
    c = a % b
    print(c)
    while not c == 0:
        a = b
        b = c
        c = a % b
    print("Mdc é ",b)
    

primos_list = []
def primos(n):
    global primos_list
    
    for i in range(0,n+1):
        primo = True
        for j in range (2,i):
            if i%j == 0:
                primo = False
                break
        if primo and not i == 0:
            primos_list.append(primo)
            print("O número ",i,' é primo.')

def inverso(a,n):
    #ax mod n = 1
    # r = ax + kn
    inverso = False
    for i in range(1,n):  
        ax = i*n + 1
        x= ax / a
        r = ax % a 
        if r == 0 and x < n :
            print("O inverso de ",a," é ",x)
            inverso = True
    if not inverso: print(a," não tem inverso.")
        
def exp_mod(a,x,n):
    r = (a*a) % n
    #print("Primeiro R ",r)
    for i in range(1,x-1):
        oldr = r
        r = (a*oldr) % n
        #print(r,"=",a,"*",oldr,"%",n)
    print(r)     

def exp_mod_otimizado(a,x,n):
    
    if math.log2(x)%1 == 0: # X Par
            r = (a*a) % n
            e = int(x/2)
            print (r)
            k = 1
            print(k,"ª interação.")
            while not e == 1:
                k = k + 1
                print(k,"ª interação.")
                oldr = r
                r = (oldr*oldr)%n
                e = int(e/2)
    else:
        if(x%2==0):
            print(exp_par(a,x,n))              
        else:
            print(exp_imp(a,x,n))             
   
def exp_imp(a,x,n):
    x = x - 1
    f = a
    r = (a*a) % n
    print("R",r)
    e = int(x/2)
    print("E",e)
    while e%2 == 0:           
        r = (r*r)%n
        e = int(e/2)
        print("R",r)
        print("E",e)
        if e == 1 or e == 0:
            print("r*a",r,a)
            return (r*a)%n

    return (exp_imp(r,e,n)*a)%n

def exp_par(a,x,n):
    x = x
    f = a
    r = (a*a) % n
    print("R",r)
    e = int(x/2)
    print("E",e)
    while e%2 == 0:           
        r = (r*r)%n
        e = int(e/2)
        print("R",r)
        print("E",e)
        if e == 1:
            print("r*a",r,a)
            return (r*a)%n
    return exp_imp(r,e,n)

set_mode(mode)
