#  1.使用课程所给方法 找出目前所学的所有 python原生 可哈希数据类型 和 不可哈希数据类型
Lst1 = [1, 1.0, '1', [1], (1,), {'1': 1}, {1}]
Lst2 = ['整数', '浮点型', '字符串', '列表', '元组', '字典', '集合']
for i in Lst1:
    try:
        hash(i)
        print(Lst2[Lst1.index(i)]+'是可哈希数据类型')
    except:
        print(Lst2[Lst1.index(i)]+'是不可哈希数据类型')


#  2.分析 高级数据类型的优缺点 尝试 使用你觉得最好的方案 表示 一个小区的住户信息  并给出代码
#     每个小区包括 4个单元  每个单元有不同数量的住户   住户有姓名，年龄，收入，描述信息
Ifo_ZhuHu = {'姓名': '博丽灵梦', '年龄': 18, '收入': 18000, '描述信息': '乐园的巫女'}
Ifo_DanYuan = [Ifo_ZhuHu]
Dic_XiaoQu = {'单元一': Ifo_DanYuan}


#  附加题 可以不做   为期两周
#      尝试写一个名片管理系统   名片信息包括  姓名、年龄、性别、联系方式、email
#      系统功能至少应该包括如下部分  可以自行更改以及新增

#    系统功能：
#         1、名片添加: 通过input输入信息，然后添加到名片系统中  这里给出采集输入信息的示例函数get_card 。完成添加后 回到系统功能选择界面
#         2、名片检索: 通过输入姓名 检索系统中是否存在对应名片  如果存在 则打印出来  否则 提示未找到 。完成检索后 回到系统功能选择界面
#         3、名片删除: 通过输入姓名 检索系统中是否存在对应名片  如果存在 则删除  否则 提示未找到。 完成删除后 回到系统功能选择界面
#         4、名片更新: 输入需要更新的名片姓名 提示可以修改的信息 如 姓名、年龄、性别、联系方式、email
#                    继续输入需要修改的子项 后 输入新信息。  完成修改后 回到系统功能选择界面
#         5、系统退出: 关闭系统
def print_card_sys():
    print('''\
---------------------------------------------------
------------------Card System v1.0-----------------
|                   1、名片添加                   |
|                   2、名片检索                   |
|                   3、名片删除                   |
|                   4、名片更新                   |
|                   5、系统退出                   |
---------------------------------------------------
''')


def get_card():
    card_info = input("请输入名片信息(字典形式):")
    try:
        #　如果输入信息可以被正确解析　则返回字典
        data = eval(card_info)
        if isinstance(data, dict):
            return data
    except:
        pass
    print("输入格式不正确")
    # 如果格式不正确 则返回空字典
    return {}


Card_Data = [{'姓名': '博丽灵梦', '年龄': 18, '性别': '女', '联系方式': '你猜', 'email': '你猜'}]
while True:
    print_card_sys()
    Selc = input('请选择：')
    if Selc == '1':
        data = get_card()
        Card_Data.append(data)
        continue
    elif Selc == '2':
        Name = input('请输入要查询的姓名：')
        count = 0
        for i in Card_Data:
            count += 1
            if i.get('姓名') == Name:
                print(i)
                break
            if count == len(Card_Data):
                print('查无此人')
    elif Selc == '3':
        Name = input('请输入要查询的姓名：')
        count = 0
        for i in Card_Data:
            count += 1
            if i['姓名'] == Name:
                Card_Data.remove(i)
                break
            if count == len(Card_Data):
                print('查无此人')
    elif Selc == '4':
        Name = input('请输入要查询的姓名：')
        count = 0
        for i in Card_Data:
            count += 1
            if i['姓名'] == Name:
                Card_Data.remove(i)
                Update = eval(input('请输入要更新的信息(字典格式):'))
                i.update(Update)
                Card_Data.append(i)
                break
            if count == len(Card_Data):
                print('查无此人')
    elif Selc == '5':
        break
