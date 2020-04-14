# Intergers
a = 4
print(a)

# type, python 3x kieu so nguyen la vo han
print(type(a))


# Float :(So thuc) Tap hop so nguyen va so thap phan
# Python 3 So thuc co do chinh xac xap xi 15 chu so thap phan
b = 1.9696969696966969696969696969
print(b)
print(type(b))

# Kieu Decinmal de lay so dai hon float

# Lay toan bo noi dung cua thu vien decimal
from decimal import*
# Lay toi da 30 chu so nguyen va phan thap phan decimal
getcontext().prec = 30

print(Decimal(10)/Decimal(3))
# Chi can mot thang decimal no se hieu cho la kieu decimal
#Lay uu tien theo do lon cua kieu du lieu

## Kieu phan so
from fractions import*
frac = Fraction(6,9)
print(frac)
print(type(frac))

frac2 = Fraction(10,3)

frac3 = frac + frac2
print(frac3)

# complex (So phuc) => LOL
# Cau truc : <Phan thuc>+<phan ao>j
c = complex(2,5) 
print(c)
# lay phan thuc
print(c.real)
#lay phan ao
print(c.imag)

## Operator (toan tu)
o = 10
y = 3

# Ket qua la mot so thuc
print(o/y)

# lam tron (ket qua luon lon hon hoac bang o chia y )
print(o//y)

# Chia lay phan du
print(o%y)

# Luy thua x voi co so y
print(o**y)

# Thu vien math trong Python
import math

print(math.trunc(3.9))