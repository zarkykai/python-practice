#find josephus out of n people when kill one out of every q people
import Reader       #文件读取方法以及Person类存储在自定义的Reader模块中

ZIPPATH = 'ADcarry.zip'
ZIP_TARGET_FILE = 'ADcarry/ADcarry.csv'
CSVPATH = 'ADcarry2/ADcarry.csv'
EXCELPATH = 'ADcarry2/ADcarry.xlsx'

STEP=3
begin_person='卡莎'

#函数实现约瑟夫环
def get_death_order(input_list, step, start_person ):
    death_list = []
    list_copy = input_list.copy()
    rem = len(list_copy)

################输入检查，输入的起始位置是否在列表中
    start_point = -1
    for x in list_copy:
        if x.name == start_person:
            start_point = list_copy.index(x)
            print('\033[0;32;40m\t start person founded \033[0m')

    if start_point == -1:
        start_point = 0             #若列表中没有找到输入的起始值，则将起始值置为0
        print('\033[0;31;40m\t start person not founded, the start person has been set to the first one \033[0m')
#################
    assert start_point >= 0
    for counter in range(len(list_copy)):
        assert step != 0
        '''判断输入的步长的正负-----------------------'''
        if step > 0:
            out_point = (start_point -1 + step )%rem

        if step < 0:
            out_point = (start_point + 1 + step) % rem
        '''-----------------------------------------------'''

        death_list.append(list_copy[out_point])
        del list_copy[out_point]

        start_point = out_point
        rem = rem -1

    return death_list

#使用迭代器类实现约瑟夫环
class JosephusRing():

    def __init__(self, ipt_list = [], step = 0, start_person = ''):
        assert  step >= 0
        assert type(ipt_list) == list
        assert  type(start_person) == str

        self.__list = ipt_list.copy()
        self.__step = step
        self.__start_person = start_person
        self.death_list = []

        ################检查起始位置是否在列表中
        self.__pointer = -1
        for x in self.__list:
            if x.name == self.__start_person:
                self.__pointer = self.__list.index(x)       #若在列表中找到,则将pointer设置为起始值的索引
                print('\033[0;32;40m\t start person founded \033[0m')

        if self.__pointer == -1:
            self.__pointer = 0  # 若列表中没有找到输入的起始值，则将pointer置为0
            print('\033[0;31;40m\t start person not founded, the start person has been set to the first one \033[0m')
        #################
    def __iter__(self):
        return self

    def __next__(self):
        # if self.__rem > 0:
        if len(self.__list) > 0:
            self.__pointer = (self.__pointer - 1 + self.__step) % len(self.__list)      #迭代公式，对索引进行运算

            self.death_list.append(self.__list[self.__pointer])     #
            del self.__list[self.__pointer]


        else:
            raise  StopIteration
        return self.death_list[len(self.death_list)-1]   #返回死亡名单中的最新一个对象

if __name__ == '__main__':
    '''调用不同的Reader进行文件读取'''
    # obj = Reader.ExcelReader(EXCELPATH)
    obj = Reader.CsvReader(CSVPATH)
    # obj = Reader.ZipReader(file_dir = ZIPPATH, target_file = ZIP_TARGET_FILE)
    list_ = obj.read()

    '''文件读取结果打印'''
    for x in list_:
        print("name:",x.name,"id:",x.id)

    '''josephus排序并打印结果(使用函数）'''
    # death_list = get_death_order(list,STEP,begin_person)
    # print('\033[0;32;40m\t the josephus death order is: \033[0m')
    # for y in death_list:
    #     print("name:", y.name, "id:", y.id)

    '''josephus排序并打印结果（使用迭代器类）'''
    JS_interable_obj = JosephusRing(list_,STEP,begin_person) #建立可迭代对象，自身就是迭代器
    print('\033[0;32;40m\t the josephus death order is: \033[0m')
    for i in JS_interable_obj:
        print("name:",i.name,"id:",i.id)
