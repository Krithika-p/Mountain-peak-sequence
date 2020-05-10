print("Enter a number N")
n=int(input())
if n>2:
    modulo=1000000007
    a=pow(2,(n-1))%modulo
    b=2%modulo
    c=b%modulo
    s=a-c
    print(s)
else:
    print("0")