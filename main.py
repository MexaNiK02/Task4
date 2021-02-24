import sys

from PyQt5 import uic  # Импортируем uic 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.db")
        self.pushButton_2.clicked.connect(self.up)
    
    def update_result(self):
        self.con = sqlite3.connect("coffee.db")
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute(f"""SELECT * FROM coffe WHERE (id > 0)""").fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        # Если запись не нашлась, то не будем ничего делать
        self.tableWidget.setColumnCount(len(result[0]))
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    
    def up(self):
        self.update_result()  


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())