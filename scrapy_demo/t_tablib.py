import  tablib

# 创建dataset1，方式一：
# dataset1 = tablib.Dataset()
# dataset1.headers = ['id','name','age','sex']
# dataset1.append(['1','朱宇','21','male'])
# dataset1.append(['2','张昊','22','male'])
# 创建dataset2，方式二：
header2 = ['id','name','password']
data = [
    ['1','杨鹏','123'],
    ['2','代松柏','567'],
]
dataset2 = tablib.Dataset(headers=header2,*data)
#增
# 增加一行数据(拿dataset2举例子)
dataset2.append(['3','朱宇','123'])
# # 增加一列数据，增加年龄这列数据(实在原有的基础上额)
dataset2.append_col((20,21,22),'age')
# # 行很多时
# import random
# def get_score(row):
#     return random.randint(60, 100)
# dataset2.append_col(get_score, headers='score')
# # 查
#     # 查看某一行的数据,例如第一行
# dataset2[0]
#     # 获取某一列的数据,获取到了score这一列的所有数据
# dataset2['score']
#     # 这是通过索引去获取列数据，和上面获取某一行是一样的
# dataset2.get_col(0)
# # 删除某行，某列
# del dataset2[0]
# del dataset2["score"]
#
# # 格式转换
# dataset2.json    # 转成json格式
# dataset2.xls     # 转成xls格式
# dataset2.csv    # 转成csv格式
#
# # Databook,如下,打开book.scv你会发现下面会有两个sheet，也就是两个文件
# book = tablib.Databook(dataset1,dataset2)
# with open ('c.csv','wb') as f:
#     f.write(book.csv)