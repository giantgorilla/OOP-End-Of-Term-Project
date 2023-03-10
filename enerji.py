from PyQt5 import QtCore, QtGui, QtWidgets
import sys, res

class Ui_Enerji(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(405, 821)
        Form.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-20, -10, 450, 867))
        self.label_2.setStyleSheet("border-radius:20px;\n"
"border-image: url(:/images/Images/background.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 360, 780))
        self.label_6.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-20, -30, 450, 900))
        self.widget.setMaximumSize(QtCore.QSize(1000, 1000))
        self.widget.setStyleSheet("QPushButton#pushButton{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{    \n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{    \n"
"    color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115, 128, 142, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(50, 780, 281, 55))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(80, 350, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(255,255,255)")
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 200, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: darkgold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0,128,128), stop:1 rgb(0, 255, 255));\n"
"border-style: solid;\n"
"border-radius:21px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Tasarim\\Images/Icon/metroikon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 310, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: darkgold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0,128,128), stop:1 rgb(0, 255, 255));\n"
"border-style: solid;\n"
"border-radius:21px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Tasarim\\Images/Icon/elektrik.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 430, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: darkgold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0,128,128), stop:1 rgb(0, 255, 255));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Tasarim\\Images/Icon/g??ne??ikon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(50, 480, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(255,255,255)")
        self.label_8.setObjectName("label_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 570, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: darkgold;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0,128,128), stop:1 rgb(0, 255, 255));\n"
"border-style: solid;\n"
"border-radius:21px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Tasarim\\Images/Icon/santral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(70, 610, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:rgb(255,255,255)")
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 77, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));border-radius:21px;")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 370, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255,255,255)")
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setGeometry(QtCore.QRect(90, 630, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(255,255,255)")
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(80, 500, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(255,255,255)")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(130, 520, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(255,255,255)")
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setGeometry(QtCore.QRect(70, 390, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgb(255,255,255)")
        self.label_13.setObjectName("label_13")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(60, 250, 360, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:rgb(255,255,255)")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(180, 270, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:rgb(255,255,255)")
        self.label_16.setObjectName("label_16")
        self.btn_geri = QtWidgets.QPushButton(self.widget)
        self.btn_geri.setGeometry(QtCore.QRect(340, 780, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.btn_geri.setFont(font)
        self.btn_geri.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
        self.btn_geri.setStyleSheet("border-image:url(:/images/Images/Icon/geri.png)")
        self.btn_geri.setText("")
        self.btn_geri.setObjectName("btn_geri")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p>?? 2022, Made With By Emir,Do??ukan,Ceyhun...</p></body></html>"))
        self.label_7.setText(_translate("Form", "??zban Yolcu ta????mac??l??????nda, kataner,"))
        self.pushButton_2.setText(_translate("Form", "Metro ve Tramvay Enerji T??ketimi"))
        self.pushButton_3.setText(_translate("Form", "??zban Elektrik T??ketimi"))
        self.pushButton_4.setText(_translate("Form", "Lisanss??z G??ne?? Enerji Santralleri"))
        self.label_8.setText(_translate("Form", "??zmir B??y??k??ehir Belediyesi b??nyesinde kurulu"))
        self.pushButton_5.setText(_translate("Form", "Bergama Elektrik ??retim Verileri"))
        self.label_11.setText(_translate("Form", "Bergama D??zenli At??k Depolama ve Enerji"))
        self.pushButton.setText(_translate("Form", "??ndirmek ??stedi??iniz Veriyi Se??iniz"))
        self.label_4.setText(_translate("Form", "bina,yolcu ba????na ve kilometre ba????na t??ketilen"))
        self.label_12.setText(_translate("Form", "??retim Tesisi elektrik ??retim veri seti."))
        self.label_9.setText(_translate("Form", "yada kurulmas?? planlanan g??ne?? enerjisi"))
        self.label_10.setText(_translate("Form", "santrallerine ili??kin bilgiler."))
        self.label_13.setText(_translate("Form", "t??ketilen elektrik miktar?? hakk??nda veri seti"))
        self.label_15.setText(_translate("Form", "Yolcu Ba????na Toplam Enerji T??ketimi (kWh)"))
        self.label_16.setText(_translate("Form", "veri seti."))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Enerji()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
