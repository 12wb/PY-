# TO编程示例    目的是 ：控制外设  
# file = open('wenjian','w',encoding='utf_8',buffering=4096)
file = open('wenjiang.txt','w')
file.write('我是第一个文件\n大家读取我吧')
file = open('wenjian.txt','r')
a = file.read()
print(a)

# 异步
file = open('yibu.txt','w',bufferifng=4096)
file.write('+'*(2090))
file.write('+'*(2090))