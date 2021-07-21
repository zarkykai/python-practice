from PyQt5.QtWidgets import *
import ConsoleUI
from JsDialogUI import JsDUI
from josephus.src.josephus import JosephusRing
from josephus.src.Reader import ExcelReader, CsvReader
from josephus.src.Person import Person


class JosephusUI(QDialog,JsDUI): # 此处类的命名应再加考虑
    def __init__(self):
        super(JosephusUI,self).__init__()
        self.setupUi(self)
        # 设置信号连接
        self.choose_file_pushButton.clicked.connect(self.slot_input_from_file)
        self.manual_input_pushButton.clicked.connect(self.slot_add_person)
        self.start_process_Button.clicked.connect(self.slot_start_process)
        self.__list = []
        self.__file_name = ''
        self.step = 0
        self.start_person = ''
        self.death_list = []

    def slot_add_person(self):
        name_ = self.name_lineEdit.text()
        id_ = self.id_lineEdit.text()
        # 检测输入内容是否合法，是否为空等
        self.__list.append(Person(name_, id_))

        for i in self.__list:
            self.ipt_list_textBrowser.append(self.__list[i])

    def slot_input_from_file(self):
        self.__file_name = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd())

        if self.__file_name.endswith('csv'):
            self.__list = CsvReader(self.__file_name).read()
        elif self.__file_name.endswith('xls') | self.__file_name.endswith('xlsx'):
            self.__list = ExcelReader(self.__file_name).read()
        else:
            print('unsupported file type')
        for i in self.__list:
            self.ipt_list_textBrowser.append(self.__list[i])

    def slot_start_process(self):
        self.step = int(self.step_lineEdit.text())
        self.start_person = self.start_person_lineEdit.text()

        interable_obj = JosephusRing(self.__list, self.step, self.start_person)
        for i in interable_obj:
            self.death_list.append(i)

        for i in self.__list:
            self.death_list_textBrowser.append(self.death_list[i])

if __name__ == '__main__':
    print('请选择使用控制台界面or图形界面')
    bool_ = input('1、控制台界面\n2、图形界面\n')
    if bool_ == '1':
        ui = ConsoleUI.JosephusUI()
    elif bool_ == '2':
        app = QApplication([])
        # 初始化
        myWin = JosephusUI()
        # 将窗口控件显示在屏幕上
        myWin.show()
        # 程序运行，sys.exit方法确保程序完整退出。
        app.exec_()
    else:
        print('error input')  # raise exception('error input')
