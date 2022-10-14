def per(a,b):
    new=""
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while a>0:

        new+=alpha[a%b]
        a=a//b
    new=new[::-1]
    return new
print(per(35,36))
