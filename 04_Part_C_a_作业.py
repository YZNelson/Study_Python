# 作业1： 有1000块钱，买鸡，
#       公鸡--3元一只，母鸡 1元一只， 小鸡--一元3只
#       要求 买的所有的鸡的数量总和为1000 钱必须用光
Lst_G = []
Lst_M = []
Lst_X = []
Times = 0
for Count_G in range(1, 334):
    for Count_M in range(1000):
        Count_X = 1000 - Count_G - Count_M
        Cost = 3 * Count_G + 1 * Count_M + 1 * (Count_X/3)
        Count = Count_G + Count_M + Count_X
        if Cost == float(1000):
            Lst_G.append(Count_G)
            Lst_M.append(Count_M)
            Lst_X.append(Count_X)
            Times += 1
for i in range(Times):
    print('公鸡数量为{}，母鸡数量为{}，小鸡数量为{}'.format(Lst_G[i], Lst_M[i], Lst_X[i]))

# 作业2： 求出 100 以内的 所有 素数
for i in range(2, 101):
    if i == 2:
        print(i, end='\t')
    else:
        for k in range(2, i+1):
            if k != i and i % k == 0:
                break
            elif k == i:
                print(i, end='\t')
