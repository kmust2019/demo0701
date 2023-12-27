from random import randint
import time

# 玩家
class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵


class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        # if self.strength == self.maxStrength:
        #     return
        self.strength += stoneCount
        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'
    # 雇佣价 100灵石，属于静态属性
    price = 100
    # 最大生命值 ，属于静态属性
    maxStrength = 100


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')



# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'
    # 雇佣价 120灵石
    price = 120
    # 最大生命值
    maxStrength = 120
    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('''
***************************************
****           游戏开始             ****
***************************************

'''
)

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '

# 显示 妖怪信息
print(notification,end='')


time.sleep(10)
for i in  range(20) :
    print('\n')
# 开始
player =Player(1000)
archer_list = []
axeman_list = []
player.warriors['ar'] = archer_list
player.warriors['ax'] = axeman_list

# 雇佣战士并命名
print('您当前所有灵石数量为 '+str(player.stoneNumber))
print('各类战士属性 '+Archer.typeName+' 价格 '+str(Archer.price)+' 生命值 '+str(Archer.maxStrength))
print('各类战士属性 '+Axeman.typeName+' 价格 '+str(Axeman.price)+' 生命值 '+str(Axeman.maxStrength))
buy_archer = int(input('请输入雇佣弓箭兵的数量'))
buy_axeman = int(input('请输入雇佣斧头兵的数量'))
player.stoneNumber = player.stoneNumber - buy_archer * Archer.price - buy_axeman * Axeman.price
# 判断输入 是否合法
while player.stoneNumber < 0 :
    print('灵石数量不足，请重新输入数量')
    buy_archer = int(input('请输入弓箭兵的数量'))
    buy_axeman = int(input('请输入斧头兵的数量'))
    player.stoneNumber -= buy_archer * Archer.price - buy_axeman * Axeman.price
else:
    # 命名后添加到对应战士列表中
    for i in range(buy_archer):
        ar_name = 'ar' + str(i)
        archer_list.append(Archer(ar_name, 100))
    for j in range(buy_axeman):
        ax_name = 'ax' + str(j)
        axeman_list.append(Axeman(ax_name, 120))

print('开始征途')
for i in range(forest_num):
    print('进入第'+str(i+1)+'座森林')
    # 展示 士兵姓名 和血量信息
    for ar in archer_list:
        print(ar.name + ' ' + str(ar.strength))
    for ax in axeman_list:
        print(ax.name + ' ' + str(ax.strength))
    # 选择出战士兵类别 和编号
    choose_type = input('请输入出战士兵类别，ar 代表弓箭兵,ax 代表斧头兵')
    choose_serial = int(input('请输入出战士兵编号，如 0 1 2 3'))
    print('该森林出场妖怪类别为'+forestList[i].monster.typeName)
    fight_list = player.warriors[choose_type]
    fight_warrior = fight_list[choose_serial]
    # 与妖怪战斗
    fight_warrior.fightWithMonster(forestList[i].monster)
    #  判断生命值
    while fight_warrior.strength <= 0 :
        # 战士死亡，从列表中移除，需要重新选择 士兵
        fight_list.pop(choose_serial)
        print('战士死亡，请重新选择出战士兵')
        for ar in archer_list:
            print(ar.name + ' ' + str(ar.strength))
        for ax in axeman_list:
            print(ax.name + ' ' + str(ax.strength))
        choose_type = input('请输入出战士兵类别，ar 代表弓箭兵,ax 代表斧头兵')
        choose_serial = int(input('请输入出战士兵编号，如 0 1 2 3'))
        fight_list = player.warriors[choose_type]
        fight_warrior = fight_list[choose_serial]
        fight_warrior.fightWithMonster(forestList[i].monster)
    else:
        # 未死亡
        print(fight_warrior.name+'成功击杀野怪'+',剩余血量'+str(fight_warrior.strength))

    # 选择是否治疗士兵
    print('剩余灵石数量为' + str(player.stoneNumber))
    healing_nums = int(input('请输入消耗灵石疗伤的数量,0代表跳过'))
    if healing_nums !=0 :
        # 扣减灵石数量，增加血量
        fight_warrior.healing(healing_nums)
        player.stoneNumber -= healing_nums
        print(fight_warrior.name  +'治疗后剩余血量' + str(fight_warrior.strength))
        print('剩余灵石数量为' + str(player.stoneNumber))
    print('进入下一座森林')

#  通关后
print('恭喜，顺利通过所有森林，玩家剩余灵石数量为'+str(player.stoneNumber))













