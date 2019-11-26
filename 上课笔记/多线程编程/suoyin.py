name = ["aa","bb","cc"]
for i in name:
    print(i)

# 标记索引序列
for i in enumerate(name):
    print(i)

# 拆包
for i,n in enumerate(name):
    print(i)
    print(n)