import  tablib

# 创建dataset1，方式一：
dataset1 = tablib.Dataset()
dataset1.headers = ['id','name','age','sex']
dataset1.append(['1','朱宇','21','male'])
dataset1.append(['2','张昊','22','male'])
# 创建dataset2，方式二：
header2 = ['id','name','password']
data = [
    ['1','杨鹏','123'],
    ['2','代松柏','567'],
]
dataset2 = tablib.Dataset(headers=header2,*data)