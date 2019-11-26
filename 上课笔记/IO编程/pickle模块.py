import pickle  # pickle: 数据序列
d = dict(name='Bob',age=20,scr=88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)  # 从数据中提取出来并显示运行
print(reborn)
