print ("Nhap a: ")
a = float(input())
print ("Nhap b: ")
b = float(input())
print("1: Cong | 2: Tru | 3: Nhan | 4: Chia | 5 Chia du || 6 Luy thua")
print("Moi nhap lua chon")
n = int(input())
if(n==1):
    tong = a +b
    print("Tong 2 so: ",tong)
elif(n==2):
    hieu = a - b
    print("Hieu 2 so: ",hieu)
elif(n==3):
    tich = a*b
    print("Tich 2 so: ",tich)
elif(n==4):
    thuong = a/b
    print("Thuong 2 so: ",thuong)
elif(n==5):
    du = a%b
    print("a % b = ",du)
elif(n==6):
    lt = a ** b
    print("a^b = ",lt )


