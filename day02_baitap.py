print("=" * 100)
print(" " * 10 + "NGÀY 2" + " " * 10)
print("=" * 100)
#print("\n")

#Bài 1 Phân loại hạnh kiểm của học sanh.
print(" " * 10 + "Bài 1: Phân loại học lực." + " " * 10)
print("\n")

diem = float(input("Nhập điểm số :"))

if diem >= 8:
    print("Học lực giỏi.")
elif diem >= 6.5:
    print("Học lực khá.")
elif diem >= 5:
    print("Học lực trung bình.")
else:
    print("Học lực yếu.")

#Bài 2 Kiểm tra năm nhuận.
print("=" * 100)
print(" " * 10 + "Bài 2: Kiểm tra năm nhuận." + " " * 10)
print("\n")

nam = int(input("Nhập năm cần kiểm tra :"))

if nam % 4 == 0:
    print(f"{nam} là năm nhuận.")
else:
    print(f"{nam} không phải là năm nhuận.")

#Bài 3 Giải phương trình bật 1.
print("=" * 100)
print(" " * 10 + "Bài 3: Giải phương trình bật 1" + " " * 10)
print("\n")

a = float(input("Nhập giá trị a = "))
b = float(input("Nhập giá trị b = "))

if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print(f"Nghiệm của phương trình x = {x}")

#Bài 4 Giải phương trình bật 2.
print("=" * 100)
print(" " * 10 + "Bài 4: Giải phương trình bật 2" + " " * 10)
print("\n")

import math
a = float(input("Nhập giá trị a = "))
b = float(input("Nhập giá trị b = "))
c = float(input("Nhập giá trị c = "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print(f"Nghiệm của phương trình x = {x}")
else:
    delta = b*b - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có 2 nghiệm x1 = {x1} và x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"phương trình có 1 nghiệm x = {x}")
    else:
        print("Phương trình vô nghiệm.")


        
#Bài 5 Tính tiền taxi.
print("=" * 100)
print(" " * 10 + "Bài 5: Tính tiền taxi" + " " * 10)
print("\n")

km = float(input("Nhập chiều dài đoạn đường : "))

if km <= 1:
    tien = km * 15000
elif km <= 5:
    tien = 1 * 15000 + (km - 1) * 13500
else:
    tien = 1 * 15000 + 4 * 13500 + (km - 5) * 11000

if km > 120:
    tien *= 0.9

print(f"Tổng tiền phải trả là {tien:,.0f} VNĐ")


#Bài 6 Sắp xếp thứ tự tăng dần.
print("=" * 100)
print(" " * 10 + "Bài 6: Sắp xếp thứ tự tăng dần" + " " * 10)
print("\n")

number1 = int(input("Nhập số thứ nhứt : "))
number2 = int(input("Nhập số thứ hai : "))
number3 = int(input("Nhập số thứ ba : "))


if number1 > number2 and number2 > number3:
    print(f"Thứ tự tăng dần là: {number1}, {number2}, {number3}")
elif number2 > number1 and number1 > number3:
    print(f"Thứ tự tăng dần là: {number2}, {number1}, {number3}")
elif number1 > number3 and number3 > number2:
    print(f"Thứ tự tăng dần là: {number1}, {number3}, {number2}")
elif number2 > number3 and number3 > number1:
    print(f"Thứ tự tăng dần là: {number2}, {number3}, {number1}")
elif number3 > number1 and number1 > number2:
    print(f"Thứ tự tăng dần là: {number3}, {number1}, {number2}")
else:
    print(f"Thứ tự tăng dần là: {number3}, {number2}, {number1}")


#Bài 7 Sắp xếp học lực giỏi, khá, trung bình, yếu.
print("=" * 100)
print(" " * 10 + "Bài 7: Sắp xếp học lực học sanh." + " " * 10)
print("\n")

hs1 = float(input("Nhập điểm trung bình của học sanh 1 : "))
hs2 = float(input("Nhập điểm trung bình của học sanh 2 : "))
hs3 = float(input("Nhập điểm trung bình của học sanh 3 : "))
#hs4 = float(input("Nhập điểm trung bình của học sanh 4 : "))
#hs5 = float(input("Nhập điểm trung bình của học sanh 5 : "))
#hs6 = float(input("Nhập điểm trung bình của học sanh 6 : "))

if hs1 >= 8.5:
    hs_gioi = hs1
    print("Học sanh 1 được loại giỏi.")
elif hs1 >= 6.5:
    hs_kha = hs1
    print("học sanh 1 được loại khá.")
elif hs1 >= 5:
    hs_tbinh = hs1
    print("học sanh 1 được loại trung bình.")
else:
    hs_yeu = hs1
    print("học sanh 1 được loại yếu.")

if hs2 >= 8.5:
    hs_gioi = hs2
    print("Học sanh 2 được loại giỏi.")
elif hs2 >= 6.5:
    hs_kha = hs2
    print("học sanh 2 được loại khá.")
elif hs2 >= 5:
    hs_tbinh = hs2
    print("học sanh 2 được loại trung bình.")
else:
    hs_yeu = hs2
    print("học sanh 2 được loại yếu.")

if hs3 >= 8.5:
    hs_gioi = hs3
    print("Học sanh 3 được loại giỏi.")
elif hs3 >= 6.5:
    hs_kha = hs3
    print("học sanh 3 được loại khá.")
elif hs3 >= 5:
    hs_tbinh = hs3
    print("học sanh 3 được loại trung bình.")
else:
    hs_yeu = hs3
    print("học sanh 3 được loại yếu.")

if hs_gioi == hs1:
    print("Chúc mừng học sanh 1 nhận được học bổng.")
elif hs_gioi == hs2:
    print("Chúc mừng học sanh 2 nhận được học bổng.")
elif hs_gioi == hs2:
    print("Chúc mừng học sanh 2 nhận được học bổng.")
else:
    print("Không ai nhận được học bổng.")


#Bài 8 Tính giá vé coi phim
print("=" * 100)
print(" " * 10 + "Bài 8: Tính giá vé coi phim." + " " * 10)
print("\n")

thu2_4 = int(input("Tổng số vé bán được từ ngày thứ 2 đến ngày thừ 4 là : "))
thu5 = int(input("Tổng số vé bán được từ ngày thứ 5 là : "))
thu6_cn = int(input("Tổng số vé bán được từ ngày thứ 6 đến ngày chúa nhựt là : "))

