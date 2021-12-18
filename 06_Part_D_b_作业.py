# 题目1 设计一个战争武器的 父类
#       该父类可用于 坦克 运输车 核潜艇
class WarWeapon:
    Lst_Amour = ['自反应装甲', '复合装甲']
    Lst_Weapon = ['三联装200mm反坦克炮', '40000mm超电磁炮']
    Dic_Ammo = {'通用电磁炮弹药': 200, '200mm链式反应炮弹': 200}

    def __init__(self):
        ...

    def CheckAmour(self):
        print('检查装甲中！')
        for i in self.Lst_Amour:
            print('现有装甲为{}'.format(i), end='')

    def CheckWeapon(self):
        print('检查武器中！')
        for i in self.Lst_Weapon:
            print('现有武器为{}'.format(i), end='')

    def CheckAmmo(self):
        print('检查弹药库存中！')
        for k, v in self.Dic_Ammo.items():
            print('弹药{},数量{}'.format(k, v))

    def Fire(self):
        UseWeapon = input('请输入要使用的武器：')
        if UseWeapon in self.Lst_Weapon:
            print('准备武器{}！开火！'.format(UseWeapon))
        else:
            print('不存在该武器！请尝试重新开火！')

    def Move(self):
        print('前进！')

    def Reload(self):
        ReloadAmmo = input('请输入要重新装填的弹药：')
        if ReloadAmmo in self.Dic_Ammo:
            self.Dic_Ammo[ReloadAmmo] = 200
            print('弹药已装填完成！')
        else:
            print('不存在该类弹药！')


class Tank(WarWeapon):
    Location = '陆地'

    def __init__(self, Lst_Amour=[], Lst_Weapon=[], Dic_Ammo=[]):
        self.Lst_Amour += Lst_Amour
        self.Lst_Weapon += Lst_Weapon
        self.Dic_Ammo.update(Dic_Ammo)

    def CheckSelf(self):
        print('正在进行例行检查！')
        print('检查完成！')


class Animal():
    Jie = '动物界'
    Men = 'Men'
    Gang = 'Gang'
    Mu = 'Mu'
    Ke = 'Ke'
    Shu = 'Shu'
    Zhong = 'Zhong'
    Name = 'Name'

    def __init__(self):
        ...

    def Ifo(self):
        print('该物种属于{}界{}门{}纲{}目{}科{}属{}种'.format(self.Jie, self.Men,
              self.Gang, self.Mu, self.Ke, self.Shu, self.Zhong))

    def Eat(self):
        print('{}吃了一口饭'.format(self.Name))

    def Drink(self):
        print('{}喝了一口水'.format(self.Name))

    def Sleep(self):
        print('{}睡觉去了'.format(self.Name))

    def Poop(self):
        print('{}拉了一泡屎'.format(self.Name))


class Horse(Animal):
    def __init__(self, Men='Men', Gang='Gang', Mu='Mu', Ke='Ke', Shu="Shu", Zhong='Zhong', Name='Name'):
        self.Men = Men
        self.Gang = Gang
        self.Mu = Mu
        self.Ke = Ke
        self.Shu = Shu
        self.Zhong = Zhong
        self.Name = Name

    def Move(self):
        print('马儿跳!马儿跳!')

    def Eat(self):
        print('马嚼了一口胡萝北')
