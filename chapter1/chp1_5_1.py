# 此处str和repr的输出结果一致，与原书中（3.4， 3.39999）不符
x = 3.4
print(x)
y = str(x)
print(y)

y = repr(x)
print(y)
