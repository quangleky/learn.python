#Bài 1 nhập tên, tuổi, lời chào,...
print("Bài 1 nhập tên, tuổi, lời chào,...")
name = input("Tên của bạn là gì? :")
age = int(input("Bạn bao nhiêu tuổi? :"))
school = input("Bạn học ở đâu? :")
     
print(f"Tui tên là {name}, năm nay tui {age} tuổi.")
print(f"Chào {name} đến với buổi học python đầu tiên.")
print(f"năm nay {name} {age} tuổi.")
print(f"{name} đang học python ở {school} với Grok.")

#Bài 2 tính chu vi, diện tích đường tròn có bán kính r
print("Bài 2 tính chu vi, diện tích đường tròn có bán kính r")
r = int(input("Nhập bán kính r :"))           #Bán kính
pi = 3.14
chu_vi = r * 2 * pi
dien_tich = r**2 * pi
print(f"Chu vi hình tròn với bán kính {r} = {chu_vi}")                #Chu vi
print(f"Diện tích hình tròn với bán kính {r} = {dien_tich}")          #Diện Tích

#Bài 3 đổi độ C thành độ F
print("Bài 3 đổi độ C thành độ F")
c = int(input("Nhập độ C :"))                           #Độ C
f = (c * 1.8) + 32
print(f"{c} độ C đổi thành {f} độ F")

#Bài 4 tính tổng, hiệu, tích, thương của 2 số a,b
print("Bài 4 tính tổng, hiệu, tích, thương của 2 số a,b")
a = int(input("Nhập số a :"))                    #Số thứ nhứt
b = int(input("Nhập số b :"))                    #Số thứ hai
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
print(f"Tổng a + b = {tong}")              #Tổng
print(f"Hiệu a - b = {hieu}")              #Hiệu
print(f"Tích a * b = {tich}")              #Tích
print(f"Thương a / b = {thuong}")          #Thương

#Bài 5 tìm số lớn nhứt trong 3 số x, y, z
print("Bài 5 tìm số lớn nhứt trong 3 số x, y, z")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
max = 0
if x > max:
    max = x
if y > max:
    max = y
if z > max:
    max = z
print(f"Số lớn nhứt là {max}")

#Bài 6 tính chỉ số BMI của nam
print("Bài 6: Tính chỉ số BMI của nam.")
chieu_cao = float(input("Nhập chiều cao :"))
can_nang = float(input("Nhập cân nặng :"))
bmi = can_nang / (chieu_cao * chieu_cao)
print(f"Chỉ số BMI của bạn là : {bmi}")
if bmi < 18.5:
    print("Bạn đang bị thiếu cân.")
if 18.5 < bmi < 23:
    print("Bạn đang có chỉ số BMI bình thường.")
if 23 < bmi:
    print("Bạn đang bị thừa cân.")

#Bài 7 Đổi thời gian
print("đổi thời gian")
giay = int(input("Nhập số giây cần đổi :"))
