# main.py
from QLSV import student

while True:
    print("Chọn chức năng:")
    print("1: Thêm sinh viên")
    print("2: Xóa sinh viên")
    print("3: Sửa thông tin sinh viên")
    print("4: Xem danh sách sinh viên")
    print("0: Thoát")

    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == '1':
        student.them_sinh_vien()
    elif lua_chon == '2':
        student.xoa_sinh_vien()
    elif lua_chon == '3':
        student.sua_sinh_vien()
    elif lua_chon == '4':
        student.xem_danh_sach_sinh_vien()
    elif lua_chon == '0':
        print("Đã thoát chương trình thành công!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.\n")