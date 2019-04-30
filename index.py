from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import MySQLdb
import sys

from PyQt5.uic import loadUiType

ui,_ = loadUiType('library.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
        self.Handle_UI_Changes()

    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.Open_Day_to_Day_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_Tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)
        self.pushButton_7.clicked.connect(self.Add_New_Book)
        self.pushButton_14.clicked.connect(self.Add_Category)


    def Handle_UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)

    ########################################
    ##############  SHOW TABS ##############
    ########################################

    def Open_Day_to_Day_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Users_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)


    #######################################
    ############# BOOKS ###################
    #######################################
    def Add_New_Book(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='Shashank@1998', db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.CurrentText()
        book_author = self.comboBox_4.CurrentText()
        book_publisher = self.comboBox_5.CurrentText()
        book_price = self.lineEdit_4.text()


    def Delete_Books(self):
        pass

    def Search_Books(self):
        pass

    def Edit_Books(self):
        pass

    #######################################
    ############# USERS ###################
    #######################################

    def Add_New_Users(self):
        pass

    def Login(self):
        pass

    def Edit_User(self):
        pass

    #######################################
    ############# SETTINGS ################
    #######################################
    def Add_Category(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='Shashank@1998', db='library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_19.text()
        self.cur.execute('''
            INSERT INTO category(category_name) values (%s)
        ''', (category_name,))

        self.db.commit()
        print ('sucessfully added category')





    def Add_Author(self):
        pass

    def Add_Publisher(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()