from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMessageBox, QWidget
from PyQt6 import uic
import re
import sys

# Lớp chứa giao diện đăng nhập
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        
        # Bắt sự kiện click chuột vào nút login
        self.btn_login.clicked.connect(self.check_login)
      
    def check_login(self):
        # Lấy thông tin email và mật khẩu từ người dùng
        email = self.username.text()
        password = self.password.text()
        
        # Kiểm tra email và mật khẩu có được nhập hay không
        if not email: 
            msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        
        # Kiểm tra email và mật khẩu có khớp với tài khoản admin hay không
        if email == "admin@ad.com" and password == "admin":
            # Nếu đăng nhập thành công, chuyển sang giao diện chính (Main)
            self.close()
            mainPage.show()  
        else:
            # Nếu đăng nhập không thành công, hiển thị thông báo lỗi
            msg_box.setText("Email hoặc mật khẩu không đúng!")
            msg_box.exec()
            

# Lớp chứa giao diện chính
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("web.ui", self)

        self.nbt.clicked.connect(self.ghe)
        
    def ghe(self):
        phim.show()
        

class Film(QtWidgets.QMainWindow):
    def __init__(self):
        super(Film, self).__init__()
        pageName = "ghe.ui"
        uic.loadUi(pageName, self)  
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #Tạo các đối tượng tương ứng với các trang giao diện
    loginPage = Login()
    loginPage.show()
    mainPage = Main()
    phim = Film()
    
    # Thiết lập hộp thoại thông báo lỗi
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    
    app.exec()
    
  
    
    
    