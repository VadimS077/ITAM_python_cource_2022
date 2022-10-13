def summation(*a):
    summ=0
    b=[]
    for i in a:
        if i<0:
            b.append(abs(i)*2)
        else:
            b.append(i)
    mx=max(b)
    summ=sum(b)/mx
    return summ

print(summation(-10,2,3,15,-4))

