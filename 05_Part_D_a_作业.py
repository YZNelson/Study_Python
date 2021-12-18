# 作业1
# 尝试定义一个类   这个类用于描述网格物体
#                       包含 物体名称  顶点数量 边数量，材质名称、网格位置
#                       包含 更改材质名、更改网格位置、打印网格所有信息 等操作
#
# 并尝试使用这个类 定义不同特征的网格物体
class Object:
    def __init__(self, Name_Object='Cube', Name_Material='White', Num_Point=8, Num_Edge=12, Position=(0, 0, 0)):
        self.Name = Name_Object
        self.Material = Name_Material
        self.Num_Point = Num_Point
        self.Num_Edge = Num_Edge
        self.Position = Position

    def Change_Material(self, Name_Material='None'):
        self.Material = Name_Material

    def Change_Position(self, Position=(0, 0, 0)):
        self.Position = Position

    def Print_Info(self):
        print('Num_Point:{}\nNum_Edge:{}'.format(
            self.Num_Point, self.Num_Edge))


# 作业2
# 尝试写出第一个blender插件
# 能够在blender中搜索到插件 并展示相关的插件信息
bl_info = {
    'name': 'Study',
    'authon': 'YZNelson',
    'description': '学习过程中的第一次尝试',
    'blender': (3, 0, 0),
    'location': '它将无处不在',
    'warning': '而我们所知的一切渺小而又可笑',
    'category': 'Study',
    'version': (0, 0, 1)
}


def register():
    print('插件安装成功！')


def unregister():
    print('插件卸载成功，下次见！')
