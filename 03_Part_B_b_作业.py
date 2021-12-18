# 1.使用循环控制打印99乘法表
import time
NumLst = list((x, y) for x in range(1, 10) for y in range(x, 10))
for i in NumLst:
    Res = i[0] * i[1]
    print('{}X{}={}'.format(i[0], i[1], Res), end='\t')
    if 9 in i:
        print()


# 2.模拟打印安装进度条
spin = '|/-\\'
for i in range(20):
    # 进度控制代码示例
    print('['+spin[i % 4] + "=" * i + ">"+']',
          float(5*i), '%' '\r',  end='')
    # ##########
    # 进度休眠
    time.sleep(.2)
print('['+'=' * 20 + '>'+']', float(5*20), '%')
