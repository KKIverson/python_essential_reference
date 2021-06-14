import sys

# f = open('foo.txt')
# line = f.readline()
# while line:
#     print(line, end='')
#     line = f.readline()
# f.close()

# open(filename)返回一个可迭代对象
# for line in open("foo.txt"):
#     print(line, end="")

f = open('foo.txt', 'w')
principal = 1000
rate = 0.05
num_years = 5
year = 1
while year <= num_years:
    principal = principal * (1 + rate)
    # print(year, principal)
    # print('{0:3d}, {1:10.2f}'.format(year, principal))
    # print的参数file=，可以直接将打印内容输出到file中
    print('{0:3d}, {1:4.2f}'.format(year, principal), end='\n', file=f)
    year += 1

# 向标准输出（屏幕）写内容
sys.stdout.write('Enter your name: ')
# 从标准输入（键盘）读取
name = sys.stdin.readline()
print(name)
