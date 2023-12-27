class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return
        self.strength += stoneCount
        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength



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

archer_list = []
axeman_list  = []
for  i in range(10) :
    ar_name = 'g'+str(i)
    archer_list.append(Archer(ar_name,100))
for  j in range(10) :
    ax_name = 'f'+str(j)
    axeman_list.append(Axeman(ax_name,120))

class Player:
    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵
class Eagle():
    typeName = '鹰妖'

player1 = Player(1000)

player1.warriors['ar'] = archer_list
player1.warriors['ax'] = axeman_list

for ar in archer_list :
    print(ar.name+' '+str(ar.strength))
for  ax in axeman_list :
    print( ax.name+' '+str(ax.strength))

choose_type = input('请输入出战士兵类别，ar 代表弓箭兵,ax 代表斧头兵')
choose_serial = int(input('请输入出战士兵编号，如 0 1 2 3'))

fight_list =player1.warriors[choose_type]
fight_warrior = fight_list[choose_serial]

print(fight_warrior.name)
print(fight_warrior.strength)

fight_warrior.fightWithMonster(Eagle())


print(fight_warrior.name)
print(fight_warrior.strength)








