#BÀI 28:
n=int(input("Nhập số nguyên dương N: "))
while n<=0:
    n=int(input("Mời nhập lại số nguyên dương N:"))
print(f"Tất cả ước của số nguyên dương {n}:")
for i in range (1,n+1):
    if n%i == 0:
        print(i, end=" ")
        
        
#BÀI 29:
n=int(input("Nhập số nguyên dương N: "))
while n<=0:
    n=int(input("Mời nhập lại số nguyên dương N:"))
tong = 0
while n>0:
    tong += n % 10
    n //= 10
print("Tổng các chữ số N nguyên dương: ",tong)


#BÀI 30:
thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
if 1<= thang <=12 and nam > 0:
    if thang in {1,3,5,7,8,10,12}:
        ngay = 31
    elif thang == 2:
        if (nam%4 == 0 and nam%100 != 00) or n%400 == 0:
            ngay = 29
            print ("Năm nhuận.")
        else:
            ngay = 28
            print ("Không phải năm nhuận.")
    else:
        ngay = 30
else:
    print("Tháng không hợp lệ.")
print(f"Năm {nam}, tháng {thang} có {ngay} ngày.")


#BÀI 31:
a=int(input("Nhập cạnh 1: "))
b=int(input("Nhập cạnh 2: "))
c=int(input("Nhập cạnh 3: "))
if (a+b>c) or (a+c>b) or (b+c>a):
    if a==b==c:
        print("3 số trên lập thành tam giác đều.")
    elif a==b or a==c or b==c:
        print("3 số trên lập thành tam giác cân.")
    elif (a**2+b**2==c**2) or (a**3+c**2==b**2) or (b**2+c**2==a**2):
        print("3 số trên lập thành tam giác vuông.")
    else:
        print("3 số trên lập thành tam giác thường.")
else:
    print("3 số trên không lập thành tam giác.")
    

#BÀI 32:
a=int(input("Quãng đường đã đi (km): "))
if a==1:
    print("Tiền cước TAXI:",15000,"đ")
elif 2<=a<=5:
    tien = 15000 + (a-1)*13500
    print("Tiền cước TAXI:",tien,"đ")
elif 6<=a<=120:
    tien = 15000 + 4*13500 + (a-5)*11000
    print("Tiền cước TAXI:",tien,"đ")
else:
    tien = 15000 + 4*13500 + (a-5)*11000
    print("Tiền cước TAXI:",0.9*tien,"đ")


#BÀI 33:
import math
n=int(input("Nhập số nguyên dương n: "))
while n<=0:
    n=int(input("Mời nhập lại số nguyên dương n:"))
a = math.sqrt(n)
if n == int(a**2):
    print(f"{n} là số chính phương.")
else: 
    print(f"{n} không là số chính phương.")
    
    
#BÀI 34:
n=int(input("Nhập số nguyên dương n: "))
while n<=0:
    n=int(input("Mời nhập lại số nguyên dương n:"))
if n == 2:
    print ("Số 2 không phải là  số nguyên tố.")
else:
    kt = True
    for i in range (2,int(n**0.5)+1):
        if n%i == 0:
            kt = False
            break
    if kt:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")


#BÀI 35:
n=int(input("Nhập số nguyên n:"))
while n<=0:
    n=int(input("Mời nhập lại số nguyên n:"))
tong = 0
for i in range(1,n+1):
    tong += i
print("S =",tong)


#BÀI 36:
n=int(input("Nhập số nguyên n:"))
while n<=0: 
    n=int(input("Mời nhập lại số nguyên n:"))
tong = 0
for i in range(1,n+1):
    tong += i**2
print("S =",tong)


#BÀI 37:
n=int(input("Nhập n chẵn:"))
while n<=0 or (n>0 and n%2 !=0):
    n=int(input("Mời nhập lại n chẵn:"))
tong = 0
for i in range(2,n+2,2):
    tong += i
print("S =",tong)


#BÀI 38:
n=int(input("Nhập n lẻ:"))
while n<=0 or (n>0 and n%2 == 0):
    n=int(input("Mời nhập lại n lẻ:"))
tich = 1
for i in range(1,n+1):
    tich *= i
print("S =",tich)


#BÀI 39:
n=int(input("Nhập n:"))
while n<=0:
    n=int(input("Mời nhập lại n:"))
tong = 0
for i in range(1,n+1):
    tong += (1/i)
print("S =",tong)


#BÀI 40:
n=int(input("Nhập n:"))
while n<=0:
    n=int(input("Mời nhập lại n:"))
tong = 0
for i in range(2,n+2,2):
    tong += 1/(2*i)
print("S =",tong)


#BÀI 41:
n=int(input("Nhập n:"))
while n<=0:
    n=int(input("Mời nhập lại n:"))
tong = 0
for i in range(1,n+1,2):
    tong += 1/(2*i+1)
print("S =",tong)


#BÀI 42:
n=int(input("Nhập n:"))
while n<=0:
    n=int(input("Mời nhập lại n:"))
tong = 0
for i in range(1,n+1):
    tong += 1/(i*(i+1))
print("S =",tong)


#BÀI 43:
n=int(input("Nhập n:"))
while n<=0:
    n=int(input("Mời nhập lại n:"))
tong = 0
for i in range(1,n+1):
    tong += i/(i+1)
print("S =",tong)


#BÀI 44:
n=int(input("Nhập n:"))
while n<=0:
    n=int(input("Mời nhập lại n:"))
tong = 0
for i in range(1,n+1):
    tong += (2*i+1)/(2*i+2)
print("S =",tong)


#BÀI 45:
n=int(input("Nhập n:"))
x=float(input("Nhập x:"))
while n<=0:
    n=int(input("Mời nhập lại n:"))
ts = 0
ms = 0
tong = 0
for i in range(1,n+1):
    ts = x**i
    ms = ms+i
    tong += ts/ms
print("S =",tong)


#BÀI 46:
bo_nghiem=[]
for x in range(1,482):
    for y in range(1,140):
        for z in range(1,108):
            if 2*z + 7*y + 9*z == 979:
                bo_nghiem += [(x,y,x)]
print(bo_nghiem)


#BÀI 47:
bo_nghiem=[]
max = 0
for x in range (1,482):
    for y in range (1,140):
        for z in range (1,108):
            if 2*x + 7*y + 9*z == 979:
                sum = x+y+z
                if sum > max:
                    max = sum
                    bo_nghiem += [(x,y,z)]
print(f"{bo_nghiem} có giá trị lớn nhất x+y+z = {max}.")


#BÀI 48:
bo_nghiem=[]
min = 979
for x in range (1,482):
    for y in range (1,140):
        for z in range (1,108):
            if 2*x + 7*y + 9*z  == 979:
                sum = x+y+z
                if sum < min:
                    min = sum
                    bo_nghiem += [(x,y,z)]
print(f"{bo_nghiem} có giá trị nhõ nhất x+y+z = {min}.")



