def les(a):
    i=1
    k=0
    while a!=0:
        a-=i
        i+=1
        k+=1
    return k
print(les(10))
