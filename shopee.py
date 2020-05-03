import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableView
from PyQt5.QtGui import QIcon
from PyQt5 import uic, QtWidgets
import sqlite3

#load both ui file
uifile_1 = 'UI/mainPage.ui'
form_1, base_1 = uic.loadUiType(uifile_1)

uifile_2 = 'UI/openPage.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

class Example(base_1, form_1):
    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.change)
        self.pushButton.clicked.connect(self.search)


    def change(self):
        self.main = MainPage()
        self.main.show()
        self.close()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def search(self):
        itemName = self.lineEdit_2.text()
        brandName = self.lineEdit_3.text()
        size = self.lineEdit_4.text()
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        if(itemName == ''):

            result = cursor.execute("SELECT * FROM `item` ORDER BY `itemname` ASC")
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            print(itemName)
            result = cursor.execute("SELECT * FROM `item` WHERE itemname=`itemName` ORDER BY `itemname` ASC")
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        cursor.close()
        sqliteConnection.close()

class MainPage(base_2, form_2):
    def __init__(self):
        super(base_2, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create)

    def database(self):

        try:
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()
            print("Database created and Successfully Connected to SQLite")
            cursor.execute("CREATE TABLE IF NOT EXISTS `item` (item_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, itemname TEXT, brandname TEXT, suppliername TEXT, size TEXT, instock TEXT, costprice TEXT, sellprice TEXT)")

            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("SQLite Database Version is: ", record)
            cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("The SQLite connection is closed")

    def create(self):

        supplierName = self.comboBox.currentText()
        itemName = self.lineEdit_2.text()
        brandName = self.lineEdit_3.text()
        size = self.lineEdit_4.text()
        inStock = self.lineEdit_5.text()
        costPrice = self.lineEdit_6.text()
        sellPrice = self.lineEdit_7.text()

        if  itemName == "" or supplierName == "" or inStock == "" or costPrice == "" or sellPrice == "":
            self.messagebox("Error", "Please complete the required field!")
        else:
            self.database()
            sqliteConnection = sqlite3.connect('SQLite_Python.db')
            cursor = sqliteConnection.cursor()
            cursor.execute("INSERT INTO `item` (itemname, brandname, suppliername, size, instock, costprice, sellprice) VALUES(?, ?, ?, ?, ?, ?, ?)", (str(itemName), str(brandName), str(supplierName), str(size), str(inStock), str(costPrice), str(sellPrice)))
            sqliteConnection.commit()
            cursor.close()
            sqliteConnection.close()

            self.messagebox("Success", "Created a data!")


    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())