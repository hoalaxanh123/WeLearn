import os
from SinhVien import SinhVien

class ThuVien(object):
    'Đây là thư viện xử lý '

    def DocFile(FileName):
        DSSV_temp = []
        try:
            with open(FileName,"r",-1,"utf-8-sig") as f:
                lines = list(f)
                for line in lines:
                    x = line.split(";")
                    SV = SinhVien(x[0],x[1],x[2],x[3])
                    DSSV_temp.append(SV)
                return DSSV_temp   
        except FileNotFoundError:
            print("Không tìm thấy file , danh sách rỗng ")
            return DSSV_temp   
    
    def GhiFile(DSSV,FileName):
        if(len(DSSV) == 0):
            print("Danh sách rỗng , không có gì để in")
            return
        else:
            with open(FileName,"w+",-1,"utf-8-sig") as f:
                for SV in DSSV:
                    print(SV.toString2(),end="",file=f)


    def XuatTieuDe():
       print("=" * 69)
       print("|{}{}|{}{}|{}{}|{}".format("ID"," " * 8,"Name"," " * 25,"Class"," " * 15,"Point"))
       print("=" * 69)

    def Xuat1SV(SV):
       print("|{}{}|{}{}|{}{}|{}".format(SV.ID," " * (10 - len(SV.ID)),SV.Name," " * (29 - len(SV.Name)),SV.Class," " * (20 - len(SV.Class)),SV.Point).strip())
       print("-" * 69)

    def XuatDSSV(DSSV):
        DSSV = sorted(DSSV, key=lambda SinhVien: SinhVien.ID)
        ThuVien.XuatTieuDe()
        for SV in DSSV:
            ThuVien.Xuat1SV(SV)
        print("\n","=" * 69)
        print("==>Tổng số sinh viên : ",len(DSSV))

    def SapXepDS(DSSV,KieuSapXep):
        if(KieuSapXep == "Theo_ID"):
            DSSV = sorted(DSSV, key=lambda SinhVien: SinhVien.ID)
        elif(KieuSapXep == "Theo_Ten"):
            DSSV = sorted(DSSV, key=lambda SinhVien: SinhVien.Name)
        elif(KieuSapXep == "Theo_Lop"):
            DSSV = sorted(DSSV, key=lambda SinhVien: SinhVien.Class)
        elif(KieuSapXep == "Theo_Diem"):
            DSSV = sorted(DSSV, key=lambda SinhVien: SinhVien.Point)
        ThuVien.XuatTieuDe()
        for SV in DSSV:
            ThuVien.Xuat1SV(SV)
        print("\n","=" * 69)
        print("==>Tổng số sinh viên : ",len(DSSV))

    def NhapDiem():
            while(True):
                var = input("Vui lòng nhập vào số điểm : ")
                try:
                    temp = float(var)
                    if(temp >= 0 and temp <= 4):
                        return var
                    else:
                        print("Vui lòng điểm trong khoảng [0-4] !")
                        os.system('pause')
                except ValueError:
                    print("Vui lòng nhập dữ liệu hợp lệ")
                    os.system('pause')

    def NhapChu(CauThongBao):
          while(True):
             var = input("Vui lòng nhập {}: ".format(CauThongBao))
             if(len(var) > 0):
                 return var
             else:
                 print("Vui lòng không bỏ trống")
                 os.system('pause')

    def KiemTraDaCoSV(ID,DSSV):
        for SV in DSSV:
                if(SV.ID == ID):
                    return True
        return False

    def Them_1_SV(SV,DSSV):
        try:
            DSSV.append(SV)
            print("Thêm thành công")
            ThuVien.XuatDSSV(DSSV)
        except ValueError:
            print("Đã sảy ra lỗi , vui lòng kiểm tra lại")

    def Xoa_1_SV(ID,DSSV):
            for SV in DSSV:
                if(SV.ID == ID):
                    print("Đã xóa  thành công học viên có ID là {} khỏi danh sách".format(ID))
                    DSSV.remove(SV)
                    return DSSV
            print("Đã sảy ra lỗi , vui lòng kiểm tra lại")
            return DSSV

    def Them_SV(DSSV):
            while(True):
                ID = ThuVien.NhapChu(" mã số sinh viên ")
                if(ThuVien.KiemTraDaCoSV(ID,DSSV)):
                     print("Đã có sinh viên trong danh sách")
                     os.system("pause")
                else:
                     break
            Name = ThuVien.NhapChu(" tên của sinh viên ")
            Class = ThuVien.NhapChu(" lớp của sinh viên ")
            Point = ThuVien.NhapDiem()
            ThuVien.Them_1_SV(SinhVien(ID,Name,Class,Point),DSSV)

    def DiemCaoNhat(DSSV):
        return max(DSSV, key=lambda SinhVien: SinhVien.Point).Point
    
    def DanhSach_SV_DiemCao(DSSV):
        return filter(lambda SinhVien : float(SinhVien.Point)==float(ThuVien.DiemCaoNhat(DSSV)),DSSV)

    def LayDSLop(DSSV):
        DS_Lop=[]
        for SV in DSSV:
            if(SV.Class not in DS_Lop):
                DS_Lop.append(SV.Class)
        return DS_Lop

    def XuatDSLop(DSLop):
        for x in range(len(DSLop)):
            print("{}. {}".format(x,DSLop[x]))

    def XemSinhVienTheoLop(DSSV):
        DSLop=ThuVien.LayDSLop(DSSV)
        if(len(DSLop)==0):
            print("Danh sách trống")
            return
        else:
            ThuVien.XuatDSLop(DSLop)
            while(True):
                LopChon = input("Vui lòng nhập tên lớp : ")
                if(len(LopChon)==0):
                    print("Không bỏ trống trường này")
                    os.system("pause")
                else:
                    return filter(lambda SinhVien : SinhVien.Class.strip()==LopChon.strip(),DSSV)

         

