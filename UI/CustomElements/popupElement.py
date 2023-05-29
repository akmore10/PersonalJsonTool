import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton,QTableWidgetItem
import pandas as pd
from  Backend.script import VideoAnalysis


class CustomPopup(QDialog):
    def __init__(self,MainWindow):
        super().__init__()
        self.initUI()
        self.JsonWin = MainWindow
    def initUI(self):
        self.setWindowTitle("File Location")
        layout = QVBoxLayout()
        self.setFixedSize(350,100)
        label = QLabel("Enter the File Location : ")
        line_edit = QLineEdit()

        # Create a button
        button = QPushButton("OK")
        button.clicked.connect(lambda: self.on_button_clicked(line_edit.text()))

        # Add the label, line edit, and button to the layout

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        # Set the layout for the dialog
        self.setLayout(layout)

    def on_button_clicked(self, text):
        data = pd.read_json(text)
        obj = VideoAnalysis(data)
        result = obj.analyze()
        self.JsonWin.tableWidget.setRowCount(len(result))
        self.JsonWin.tableWidget.setVerticalHeaderLabels(["" for _ in range(len(result))])
        self.JsonWin.tableWidget.setColumnCount(4)
        self.JsonWin.tableWidget.setHorizontalHeaderLabels(["Name" , "Views" , "Link" , "Video"])
        

        for indx,res in enumerate(result):
            item = QTableWidgetItem(res.name)
            self.JsonWin.tableWidget.setItem(indx , 0,item)

            item = QTableWidgetItem(str(res.views))
            self.JsonWin.tableWidget.setItem(indx , 1,item)

            item = QTableWidgetItem(res.link)
            self.JsonWin.tableWidget.setItem(indx , 2,item)

            item = QTableWidgetItem(res.video)
            self.JsonWin.tableWidget.setItem(indx , 3,item)
            
        self.close()