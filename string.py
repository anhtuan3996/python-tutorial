"""
Day la chu thich
Muon ghi gi thi ghi
La qua huhu
"""
# Chuoi nhay don, hihi
chuoi = 'Chuoi co day nhay don'
print(chuoi)
print(type(chuoi))

chuoiNhayKep = "Chuoi nhay kep hihi"
print(chuoiNhayKep)
print(type(chuoiNhayKep))

# Chuoi nam trong ba dau nhay don
chuoiNamtrongBaNhayDon = '''Chuoi nam trong 3 nhay don (omg what's happening ?)
 Lalaalaalalal
 Lolhoho
 hodosdosdosds
'''
print(chuoiNamtrongBaNhayDon)
print(type(chuoiNamtrongBaNhayDon))
#Chuoi nam trong dau nhay kep
chuoiNamTrongBaDauNhayKep = """ Haha lai chuoi trong ba dau nhay kep nua, omg 
huhuhuhuhuhuh
hihihihihihhi
ahahahahahaha
"""
print(chuoiNamTrongBaDauNhayKep)
print(type(chuoiNamTrongBaDauNhayKep))

# Chuoi tran khong quan tam ki tu dac b
print(r'Hiaz, \n neu mot ngay nao do')

# Noi chuoi
strA = "Day la chuoi 1"
strB = 'Day la chuoi 2'
strC = strA + strB

print(strC)

# Toan tu nhan chuoi
strChuoiDeNhan = "Day la chuoi 1 thoi"
strNhan = strChuoiDeNhan * 5
print(strNhan)

# Toan tu (in) kiem tra xem x co ton tai trong y khong
strContainer = "hihih day ne"
strEl ="day"
strCheck = strEl in strContainer
print(strCheck)

'''
Trong python chuoi se duoc danh index tu 0 cho den n-1
tu trai qua phai, voi n la so ki tu co trong chuoi
'''
vidu = 'abc xyz'
print(vidu[1]) # Lay trai qua phai
print(vidu[-1]) # Lay phai qua trai
print(vidu[len(vidu) - 1])

# Slicing
sliecing = "Hello world"
print(sliecing[2:5])

#String method
stringMethod = " Hello world "
print(stringMethod)
print(stringMethod.strip())

#string format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))