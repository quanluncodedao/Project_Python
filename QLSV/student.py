# student.py
from QLSV import data

def them_sinh_vien():
    ma_sv = input("Nhập mã số sinh viên: ")
    ten_sv = input("Nhập tên sinh viên: ")
    nam_sinh = input("Nhập năm sinh của sinh viên: ")
    khoa = input("Nhập khoa của sinh viên: ")
    sinh_vien = {"Mã SV": ma_sv, "Tên SV": ten_sv, "Năm sinh": nam_sinh, "Khoa": khoa}
    data.students.append(sinh_vien)
    print("Thêm sinh viên thành công!\n")

def xoa_sinh_vien():
    ma_sv = input("Nhập mã số sinh viên cần xóa: ")
    for sinh_vien in data.students:
        if sinh_vien["Mã SV"] == ma_sv:
            data.students.remove(sinh_vien)
            print("Xóa sinh viên thành công!\n")
            return
    print("Không tìm thấy sinh viên!\n")

def sua_sinh_vien():
    ma_sv = input("Nhập mã số sinh viên cần sửa: ")
    for sinh_vien in data.students:
        if sinh_vien["Mã SV"] == ma_sv:
            sinh_vien["Tên SV"] = input("Nhập tên mới: ")
            sinh_vien["Năm sinh"] = input("Nhập năm sinh mới: ")
            sinh_vien["Khoa"] = input("Nhập khoa mới: ")
            print("Sửa thông tin sinh viên thành công!\n")
            return
    print("Không tìm thấy sinh viên!\n")

def xem_danh_sach_sinh_vien():
    if not data.students:
        print("Danh sách sinh viên trống.\n")
    else:
        print("Danh sách sinh viên:")
        for sinh_vien in data.students:
            print(sinh_vien)
        print()