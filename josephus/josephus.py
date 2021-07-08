#find josephus out of n people when kill one out of every q people
step=3
total = 10
list=[]
death_list=[]
begin_person=0
#recursion
'''
def find_josephus(n,q):
    if n==1:
        alive_one = 0
    else:
        alive_one = (find_josephus(n-1,q)+q) % n
    return alive_one

#iteration
def find_josephus2(n,q):
    alive_one=0
    for i in range(n):
        alive_one = (alive_one + q)%(i+1)
    return alive_one
'''

class person:
    name='none'
    id = 'none'

    def __init__(self,name = 'none',id = 'none'):
        self.name = name
        self.id = id

    def change_name_to(self,new_name):
        self.name = new_name
        return None

    def change_id_to(self,new_id):
        self.id = new_id
        return None


def death_order(input_list,step,start_person):
    list_copy = input_list.copy()
    rem = len(list_copy)
################输入检查
    start_point = -1
    for x in list_copy:
        if x.name == start_person:
            start_point = list_copy.index(x)
            print('start person founded')

    if start_point == -1:
        start_point = 0
        print('start person not founded, the start person will be set to the first one')
#################遍历运算
    for counter in range(len(list_copy)):
        out_point = (start_point -1 + step )%rem
        death_list.append(list_copy[out_point])
        del list_copy[out_point]

        start_point = out_point
        rem = rem -1

    return death_list

if __name__ == '__main__':
#生成一个列表,测试数据为for循环生成，total应小于60
    for num in range(total):
        a = person(name = chr(65 + num),id = num)  #名字为A,B,C,……id为0,1,2……
        list.append(a)



    for x in list:
        print("name:",x.name,"id:",x.id)
    for y in death_order(list,step,begin_person):
        print("name:",y.name,"id:",y.id)