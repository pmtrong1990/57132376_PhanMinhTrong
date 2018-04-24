print("Nhap vao 1 day so N")
number = int(input())
tong = 0
tam = 0
if(number ==0):
    print
else:
    print("Day vua nhap: ",number)
    while(number<0):
        k=number%10
        number=number/10
        if((k%2)==0):
            print (k)
            tong = tong + k
            print ("Tong cac so chan la: ",tong)
