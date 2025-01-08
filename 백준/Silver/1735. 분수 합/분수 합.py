import math

a,b=input().split()
x,y=input().split()

a=int(a)
b=int(b)
x=int(x)
y=int(y)

numerator=a*y+x*b
denominator=b*y


def gcd(denominator,numerator):
    if numerator==0:
        return denominator
    else:
        return gcd(numerator,denominator%numerator)

number=gcd(denominator,numerator)
numerator//=number
denominator//=number

print(numerator,denominator)