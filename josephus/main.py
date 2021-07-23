import sys
import os

from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog

from ui.ConsoleUI import JosephusUI
from ui.JsDialogUI import JsDUI
from src.josephus import JosephusRing
from src.Reader import ExcelReader, CsvReader
from src.Person import Person


class JSUI(QDialog, JsDUI): # 此处类的命名应再加考虑
    def __init__(self):
        super(JSUI, self).__init__()
        self.setupUi(self)

        self.__list = []
        self.__file_name = ''
        self.step = 0
        self.start_person = ''
        self.death_list = []

        # 设置信号连接
        self.choose_file_pushButton.clicked.connect(self.slot_input_from_file)
        self.manual_input_pushButton.clicked.connect(self.slot_add_person)
        self.start_process_Button.clicked.connect(self.slot_start_process)

    def slot_add_person(self):
        name_ = self.name_lineEdit.text()
        id_ = self.id_lineEdit.text()
        # 检测输入内容是否合法，是否为空等
        self.__list.append(Person(name_, id_))

        self.ipt_list_textBrowser.append('name:'+self.__list[-1].name+'   '+'id:'+self.__list[-1].id)

    def slot_input_from_file(self):
        self.__file_name, _ = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd())

        if self.__file_name.endswith('csv'):        # 将读取出来的列表拼接到list上
            self.__list = CsvReader(self.__file_name).read()
        elif self.__file_name.endswith('xls') | self.__file_name.endswith('xlsx'):
            self.__list = ExcelReader(self.__file_name).read()
        else:
            print('unsupported file type')
            self.ipt_list_textBrowser.clear()
        for i in self.__list:
            self.ipt_list_textBrowser.append('name:'+i.name+'   '+'id:'+i.id)

    def slot_start_process(self):
        self.step = int(self.step_lineEdit.text())
        self.start_person = self.start_person_lineEdit.text()

        interable_obj = JosephusRing(self.__list, self.step, self.start_person)
        for i in interable_obj:
            self.death_list.append(i)

        self.death_list_textBrowser.clear()
        for i in self.death_list:
            self.death_list_textBrowser.append('name:'+i.name+'   '+'id:'+i.id)

if __name__ == '__main__':
    print('请选择使用控制台界面or图形界面')
    bool_ = input('1、控制台界面\n2、图形界面\n')
    if bool_ == '1':
        ui = ConsoleUI.JSUI()
    elif bool_ == '2':
        app = QApplication([])
        # 初始化
        myWin = JSUI()
        # 将窗口控件显示在屏幕上
        myWin.show()
        # 程序运行，sys.exit方法确保程序完整退出。
        app.exec_()
    else:
        print('error input')  # raise exception('error input')
