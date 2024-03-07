# hcn_test.py
import hcn

chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))

chu_vi = hcn.tinh_chu_vi(chieu_dai, chieu_rong)
dien_tich = hcn.tinh_dien_tich(chieu_dai, chieu_rong)

print("Chu vi của hình chữ nhật là:", chu_vi)
print("Diện tích của hình chữ nhật là:", dien_tich)