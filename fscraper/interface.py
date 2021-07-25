
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

from scraper import scrap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("FScraper")
        MainWindow.setEnabled(True)
        MainWindow.resize(808, 734)
        MainWindow.setWindowIcon(QIcon('icon.png'))
        MainWindow.setStyleSheet("background-color: #2a2a72;\n"
                                 "background-image: linear-gradient(315deg, #2a2a72 0%, #009ffd 74%);\n"
                                 "color: #fff;\n"
                                 "font-family: \"Times New Roman\";\n"
                                 )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 70, 391, 91))
        self.label.setStyleSheet("font-size: 42px;\n"
                                 "font-weight: bold;\n"
                                 "padding-left: 70px;\n"
                                 "color: #FF7600;\n"
                                 "border: 4px solid #eee;\n"
                                 )
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 240, 431, 71))
        self.lineEdit.setStyleSheet("background-color: whitesmoke;\n"
                                    "border: 2px solid gray;\n"
                                    "font-size: 24px;\n"
                                    "color: rgba(62, 33, 93, 0.8);")
        self.lineEdit.setPlaceholderText('Enter web url')
        self.lineEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 240, 171, 71))
        self.label_2.setStyleSheet("font-size: 32px;\n"
                                   "font-weight: bold;\n"
                                   )
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 360, 181, 71))
        self.label_3.setStyleSheet("font-size: 32px;\n"
                                   "font-weight: bold;\n"
                                   )
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 360, 431, 71))
        self.lineEdit_2.setStyleSheet("background-color: whitesmoke;\n"
                                      "border: 2px solid gray;\n"
                                      "font-size: 24px;\n"
                                      "color: rgba(62, 33, 93, 0.8);")
        self.lineEdit_2.setPlaceholderText('Class name without  " "')
        self.lineEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 480, 181, 71))
        self.label_4.setStyleSheet("font-size: 32px;\n"
                                   "font-weight: bold;\n"
                                   )
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 480, 431, 71))
        self.lineEdit_3.setStyleSheet("background-color: whitesmoke;\n"
                                      "border: 2px solid gray;\n"
                                      "font-size: 24px;\n"
                                      "color: rgba(62, 33, 93, 0.8);")
        self.lineEdit_3.setPlaceholderText('HTML Element without  " "')
        self.lineEdit_3.setObjectName("textEdit_3")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 620, 341, 61))
        self.pushButton.setStyleSheet("background-color: rgb(255, 118, 0);\n"
                                      "color: whitesmoke;\n"
                                      "font-size: 28px;\n"
                                      "font-weight: bold;\n"
                                      "border: none;\n"
                                      "")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.operate)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FScraper 🔍 "))
        self.label_2.setText(_translate("MainWindow", "URL:"))
        self.label_3.setText(_translate("MainWindow", "Class:"))
        self.label_4.setText(_translate("MainWindow", "ELEMENT:"))
        self.pushButton.setText(_translate("MainWindow", "GET DATA"))

    def showDialog(self, title, msg):
        self.msgBox = QMessageBox()
        self.msgBox.setWindowTitle(title)
        self.msgBox.setText(msg)
        self.msgBox.exec()

    def operate(self):
        url = self.lineEdit.text()
        class_name = self.lineEdit_2.text()
        html_element = self.lineEdit_3.text()

        if url and class_name and html_element:
            self.pushButton.setEnabled(False)
            scrap(url, class_name, html_element)
            self.showDialog(
                "Success", "A csv file contains scraped data has been created")
        else:
            self.showDialog("No Enteries", "Please fill all fields")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
