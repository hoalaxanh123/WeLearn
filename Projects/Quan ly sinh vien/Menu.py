from ThuVien import ThuVien
from SinhVien import SinhVien
import os
class Menu:
    'Lớp menu của hệ thống'

    ListSV = []

    def XuatMenu():
        print("=" * 65)
        print("{} Hệ thống quản lý sinh viên {}".format("=" * 19,"=" * 18))
        print("=" * 65)
        print("0. Thoát chương trình")
        print("1. Đọc danh sách sinh viên")
        print("2. Xuất danh sách sinh viên")
        print("3. Thêm một sinh viên")
        print("4. Xóa một sinh viên")
        print("5. Ghi danh sách xuống file")
        print("6. Sắp xếp danh sách tăng dần theo tên")
        print("7. Sắp xếp danh sách tăng dần theo lớp")
        print("8. Sắp xếp danh sách tăng dần theo điểm")
        print("9. Sắp xếp danh sách tăng dần theo mã")
        print("10. Cho biết sinh viên có điểm cao nhất")
        print("11. Xem sinh viên theo lớp")
        print("=" * 65)

    def ChonMenu(SoMenu):
        os.system("cls")
        while(True):
            os.system('cls')
            Menu.XuatMenu()
            var = input("vui lòng lòng chọn chức năng : ")
            if(var.isnumeric() and int(var) >= 0 and int(var) <= SoMenu):
                return var
            else:
               print("Không hợp lệ vui lòng nhập lại")
               os.system('pause')

    def XuLyMenu(menu):
        #Khai báo sử dụng biến global
        global ListSV
        #Nếu danh sách chưa khởi tạo thì nạp danh sách từ file
        try:
                ListSV
        except NameError:
                ListSV=ThuVien.DocFile("DSSV.txt")
        #Xử lý menu theo chọn lựa tương ứng
        if(menu == 0):
            print("Chào tạm biệt !!!")
            exit()
        elif(menu == 1):
            os.system("cls")
            print("1. Đọc danh sách sinh viên từ file")
            FileName=input("Vui lòng nhập vào tên file : ")
            while(True):
                if(len(FileName)==0):
                    print("Vui lòng không bỏ trống")
                    os.system("pause")
                else:
                    break
            ListSV = ThuVien.DocFile(FileName)
            ThuVien.XuatDSSV(ListSV)
            print("Đọc danh sách thành công".upper())
        elif(menu == 2):
            os.system("cls")
            print("2. Xuất danh sách sinh viên")
            ThuVien.XuatDSSV(ListSV)
        elif(menu == 3):
            os.system("cls")
            print("3. Thêm một sinh viên")
            ThuVien.Them_SV(ListSV)
        elif(menu == 4):
            os.system("cls")
            print("4. Xóa một sinh viên")
            try:
                ListSV
                ThuVien.XuatDSSV(ListSV)
                ID = ThuVien.NhapChu(" mã số sinh viên ")
                ListSV = ThuVien.Xoa_1_SV(ID,ListSV)
                ThuVien.XuatDSSV(ListSV)
            except NameError:
                print("Danh sách sinh viên đang rỗng , vui lòng kiểm tra lại")
        elif(menu == 5):
            os.system("cls")
            print("5. Ghi danh sách sinh viên xuống file")
            FileName=input("Vui lòng nhập vào tên file : ")
            while(True):
                if(len(FileName)==0):
                    print("Vui lòng không bỏ trống")
                    os.system("pause")
                else:
                    break
            ThuVien.GhiFile(ListSV,FileName)
            print("File đã ghi")
        elif(menu == 6):
            os.system("cls")
            print("6. Sắp xếp danh sách tăng dần theo tên")
            ThuVien.SapXepDS(ListSV,"Theo_Ten")
        elif(menu == 7):
            os.system("cls")
            print("7. Sắp xếp danh sách tăng dần theo lớp")
            ThuVien.SapXepDS(ListSV,"Theo_Lop")
        elif(menu == 8):
            os.system("cls")
            print("8. Sắp xếp danh sách tăng dần theo điểm")
            ThuVien.SapXepDS(ListSV,"Theo_Diem")
        elif(menu == 9):
            os.system("cls")
            print("9. Sắp xếp danh sách tăng dần theo mã")
            ThuVien.SapXepDS(ListSV,"Theo_ID")
        elif(menu == 10):
            os.system("cls")
            print("10. Cho biết sinh viên có điểm cao nhất")
            print("\nMức điểm cao nhất mà học viên có trong danh sách đạt được là :",ThuVien.DiemCaoNhat(ListSV))
            print("Thông tin các học viên có mức điểm này : ")
            ThuVien.XuatDSSV(ThuVien.DanhSach_SV_DiemCao(ListSV))
            print(ThuVien.XuatDSLop(ThuVien.LayDSLop(ListSV)))
        elif(menu == 11):
            os.system("cls")
            print("11. Xem danh sách sinh viên theo lớp")
            KQ=ThuVien.XemSinhVienTheoLop(ListSV)
            ThuVien.XuatDSSV(KQ)
        os.system('pause')
        