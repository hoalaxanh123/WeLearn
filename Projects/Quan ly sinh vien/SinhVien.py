class SinhVien(object):
    "Đây là class sinh viên"

    #Khai báo thuộc tính
    ID = ""
    Name = ""
    Class = ""
    Point = ""

    #Định nghĩa hàm khởi tạo
    def __init__(self,ID,Name,Class,Point):
        self.ID = ID
        self.Name = Name
        self.Class = Class
        self.Point = Point
    #Định nghĩa hàm trả về thông tin của Sinh viên
    def toString(self):
        return ("ID : {} , Name: {} , Class : {}, Point: {}".format(self.ID,self.Name,self.Class,self.Point))

    def toString2(self):
        return ("{};{};{};{}".format(self.ID,self.Name,self.Class,self.Point))

    #Các hàm gán dữ liệu cho thông tin của sinh viên
    def SetID(self, ID):
        self.ID = ID

    def SetName(self, Name):
        self.Name = Name

    def SetClass(self, Class):
        self.Class = Class

    def SetPoint(self, Point):
        self.Point = Point

    #Các hàm lấy thông tin của sinh viên
    def GetID(self):
        return self.ID

    def GetName(self):
        return  self.Name

    def GetClass(self):
         return self.Class

    def setPoint(self):
        return Gelf.Point



