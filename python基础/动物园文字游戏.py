from random import randint
import time

# 老虎
class Tiger():
    typeName = '老虎'
    # 初始化参数是编号，体重
    def __init__(self, serial, weight):
        self.serial = serial
        self.weight = weight
    #  喂食
    def feed(self, food_type):
        if food_type == 'meat':
            print('输入正确，体重加10')
            self.weight += 10
        else:
            print('输入错误，体重减10')
            self.weight -= 10

    #  敲门
    def  knockDoor(self):
        print('Wow !!')
        self.weight -= 5

# 羊

class Sheep():
    typeName = '羊'
    # 初始化参数是编号，体重
    def __init__(self, serial, weight):
        self.serial = serial
        self.weight = weight
    #  喂食
    def feed(self, food_type):
        if food_type == 'grass':
            print('输入正确，体重加10')
            self.weight += 10
        else:
            print('输入错误，体重减10')
            self.weight -= 10
    #  敲门
    def knockDoor(self):
        print('mie~~')
        self.weight -= 5
        print('体重减5')


print('''
***************************************
****           游戏开始             ****
***************************************
'''
)
# 房间数量
room_num = 10
# 房间 列表
roomList = []
# 为每个房间 放入 老虎 或者 羊
notification = '前方房间里的妖怪是：'  # 显示在屏幕上的内容
for i in range(room_num):
    typeName = randint(0,1)
    if typeName == 0:
        serial = 'ti'+str(i)
        roomList.append(Tiger(serial,200))
    else:
        serial = 'sh' + str(i)
        roomList.append(Sheep(serial,100))
    notification += \
        f'第{i+1}个房间里面是 {roomList[i].typeName}  '

# 显示房间信息
print(notification,end='')

# 显示一段时间后 消失
time.sleep(5)
for i in  range(20) :
    print('\n')


for  i  in range(10) :
        #  随机给出房间号
        room_serial = randint(1,10)
        animal = roomList[room_serial-1]
        print('第'+str(i+1)+'次')
        print('随机抽取到第'+str(room_serial)+'号房间，请回忆该房间动物类别')
        action_choice = input('请选择敲门，还是喂食')
        if action_choice =='喂食' :
            food_choice = input('请选择meat/grass')
            animal.feed(food_choice)
        elif action_choice =='敲门' :
            animal.knockDoor()
        else:
            print('无法识别')

print('游戏结束')
for  animal in  roomList :
    print('动物编号'+animal.serial+'，体重为'+str(animal.weight))




