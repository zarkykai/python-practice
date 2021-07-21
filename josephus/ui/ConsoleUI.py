from josephus.src.josephus import JosephusRing
from josephus.src.Reader import ExcelReader, CsvReader
from josephus.src.Person import Person
# from PyQt5.QtWidgets import *
import os


class JosephusUI:
    def __init__(self):
        self.__file_name = ''
        self.__list = []
        self.__step = 0
        self.__begin_person = ''
        self.cwd = os.getcwd()

        while 1:
            self.main_process()

            bool_ = input('是否退出？若否则回到程序开始（y/n）')
            if bool_ == 'y':
                break
            elif bool_ == 'n':
                pass
            else:
                print('error input')

    def read_file_by_dialog(self):
        # obj = QFileDialog()       #想要使用文件对话框选择并打开文件,但除了使用按钮连接的方式，似乎无法直接使用文件对话框
        # obj.setFileMode(QFileDialog.AnyFile)
        # obj.setFilter('(*.csv *.xls *.xlsx )')
        # if obj.exec():
        #     self.__file_name = obj.selectedFiles()

        # self.__file_name, filetype = obj.getOpenFileName(obj, "选取文件", self.cwd, "All Files (*);;Text Files (*.txt)")

        # self.__file_name = filedialog.askopenfilename()

        print(os.listdir('../test/ADcarry2'))

        file_name = input('请选择要打开的文件（请直接将上面的文件名复制下来使用）：')
        self.__file_name = '../test/ADcarry2' + '/' + file_name
        # 此处应添加assert限制所选文件类型

        print(file_name)
        if file_name.endswith('csv'):
            self.__list = CsvReader(self.__file_name).read()
        elif file_name.endswith('xls') | self.__file_name.endswith('xlsx'):
            self.__list = ExcelReader(self.__file_name).read()
        else:
            print('unsupported file type')
            self.__list = []

        return None

    def get_list(self):
        while 1:
            bool_ = input('是否要选择文件以读取名单（y/n）:')
            if bool_ == 'y':
                self.read_file_by_dialog()
                break
            elif bool_ == 'n':
                while 1:
                    bool__ = input('是否手动输入信息（y/n）')
                    if bool__ == 'n':
                        break

                    elif bool__ == 'y':
                        name_ = input('请输入姓名：')
                        id_ = input('请输入学号：')
                        self.__list.append(Person(name_, id_))
                        self.show_list()

                    else:
                        print('error input')

                break

            else:
                print('error input')

        self.show_list()

    def show_list(self):
        print('-----------------------------')
        print('list:\n')
        for i in self.__list:
            print("name:", i.name, "id:", i.id)
        print('-----------------------------')

    def set_step_and_start_person(self):
        self.show_list()
        self.__step = int(input('设置步长为：'))
        self.__begin_person = input('设置第一个报数人：')

    def main_process(self):
        '''输入list的获取'''
        while 1:
            self.get_list()
            bool_ = input('名单输入是否完成？若是则启动算法进行重新排序（y/n）')
            if bool_ == 'y':
                break

        '''设置步长与起始人'''
        self.set_step_and_start_person()

        '''运行约瑟夫环算法'''
        interable_obj = JosephusRing(self.__list, self.__step, self.__begin_person)
        '''打印结果'''
        print('-----------------------------')
        print('\033[0;32;40m\t the josephus death order is: \033[0m')
        for i in interable_obj:
            print("name:", i.name, "id:", i.id)
        print('-----------------------------')

    def save_file_to(self):
        pass        #csv与xls文件的写操作


if __name__ == '__main__':
    JSui = JosephusUI()

