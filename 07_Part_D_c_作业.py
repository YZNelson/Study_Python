# 练习1: 课程中讲到的4种python高级功能
#       并查阅搜索引擎 列举每种高级功能的用处


# 练习2: 控制 blender的数据块  增删改查
# 创建两个脚本
# 首先手动在场景中新建一堆物体
# 脚本1:
# 将这些物体的位置随机打乱

# 脚本2:
# 将这些物体的位置按照 正弦曲线排列
# 例如 从前面看过去是正弦曲线 或者 从左面看过去是正弦曲线

# Script_All:
import bpy
import random
import math
Now_Col = bpy.context.collection
Num_Obj = 10
New_Obj_Data = bpy.context.object.data
for i in range(Num_Obj):
    New_Obj_Name = 'New_Obj_' + str(i)
    New_Obj = bpy.data.objects.new(New_Obj_Name, object_data=New_Obj_Data)
    Now_Col.objects.link(New_Obj)

# Script_01
Scale = 10
for Obj in bpy.data.objects:
    New_Location = (Scale*random.random(), Scale *
                    random.random(), Scale*random.random())
    Obj.location = New_Location

# Script_02
Pi = math.pi
Max_Scale = 100
X = 'x'
Y = 'y'
for Obj in bpy.data.objects:
    New_Loc_X = 360 * random.random()
    New_Loc_Y = Max_Scale * math.sin(math.radians(New_Loc_X))
    if X == 'x' and Y == 'y':
        Obj.location.x = New_Loc_X
        Obj.location.y = New_Loc_Y
    elif X == 'x' and Y == 'z':
        Obj.location.x = New_Loc_X
        Obj.location.z = New_Loc_Y
    elif X == 'y' and Y == 'x':
        Obj.location.y = New_Loc_X
        Obj.location.x = New_Loc_Y
    elif X == 'y' and Y == 'Z':
        Obj.location.y = New_Loc_X
        Obj.location.z = New_Loc_Y
    elif X == 'z' and Y == 'x':
        Obj.location.z = New_Loc_X
        Obj.location.x = New_Loc_Y
    else:
        Obj.location.z = New_Loc_X
        Obj.location.y = New_Loc_Y
