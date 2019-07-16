#_*_ coding:utf-8 _*_
import os
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]

# 读取用户名和密码
f = open("username.txt",'r',encoding='utf-8')
data = f.read()
f.close()
data = eval(data)

# 初始化用户购买的商品　如：[['电脑', 1999], ['鼠标', 10],]
list1 =[]

# 存放用户的消费记录　如：{ nusername:[ [[商品],余额] , ]}
dict1 ={}

# 创建新的文件名buyinfo.txt
if not os.path.exists("buyinfo"):
    f = open("buyinfo",'w',encoding='utf-8')
    f.write('')
    f.close()

# 读取用户购买的信息
f2 = open('buyinfo','r',encoding = 'utf-8' )
data2 = f2.read()
f2.close()
if len(data2) != 0:
    data2 = eval(data2)


username1 = input("请输入用户名：").strip()
password1 = input("请输入密码：").strip()
if username1 in list(data.keys()):
    if password1 == data[username1]:

        # 如果用户名在文件data2中，存在数据
        if len(data2) != 0:
            if username1 in list(data2.keys()) :
                salary = data2[username1][1]
                print("\033[31;1m用户上一次购买的商品\033[0m".center(30,'-'))
                for i in data2[username1][0]:
                    print("\033[31;1m %s %s \033[0m" % (i[0] ,i[1] ))
                print("\033[31;1m 用户的余额%s \033[0m" % salary )

            # 如查用户名在文件data2不存在
            else:
                while True:
                    salary = input("请输入工资：").strip()
                    if salary.isdigit():
                        salary = int(salary)
                        break
                    else:
                        print("用户输入的工资不合法．....")

        # 如果文件data2是空文件
        else:
            while True:
                salary = input("请输入工资：").strip()
                if salary.isdigit():
                    salary = int(salary)
                    break
                else:
                    print("用户输入的工资不合法．")

        for i, j in enumerate(goods, 1):
            print(i, j['name'],j['price'])

        while True:
            num = input("请输入购买商品的编号：").strip()
            if num.isdigit():   # 判断如果是数字时
                num = int(num) - 1
                if num in range(len(goods)):

                    if salary >= goods[num]["price"] :
                        salary -= goods[num]["price"]
                        list1.append( [ goods[num]["name"] ,goods[num]["price"] ] )
                        print("\033[31;1m用户的余额：%s，购买的商品：%s\033[0m" % (salary ,goods[num]["name"] ))
                    else:
                        print("用户的余额不足．")

                else:
                    print("\033[31;1m购买的商品的编号不存在\033[0m")

            elif num.lower() == 'b' or num.lower() == 'q': # 如果是b或q时，退出
                print("用户购买的商品是".center(30,'-'))
                print(list1)
                for i in list1:
                    print("\033[31;1m %s  %s \033[0m"  % (i[0], i[1]))
                print("用户的余额是：\033[31;1m %s \033[0m" % salary)

                f = open("buyinfo",'w+',encoding='utf-8')
                if len(data2) != 0:
                    data2[username1][0].extend(list1)
                    data2[username1][1] = salary
                    f.write(str(data2))
                else:
                    dict1[username1] = [list1, salary]
                    f.write(str(dict1))
                f.close()


                break





































