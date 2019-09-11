from Menu import Menu
from ThuVien import ThuVien

def Run():
    while(True):
        SoMenu = Menu.ChonMenu(11)
        Menu.XuLyMenu(int(SoMenu))
Run()
