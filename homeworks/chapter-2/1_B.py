def summation(a,b):
    sum=0
    g=0
    if b<a:
        g=b
        b=a
        a=g


    for i in range(a,b+1):
        sum+=i
    return sum
print(summation(12,2))