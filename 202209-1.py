n,m = input().split()#n个题目
aread = input().split()#每题正确选项
a = []

# print(n,m)
n = int(n)
m = int(m)
# print(type(n))
# print(aread)
# n = int(nm[0])
# m = int(nm[1])
for i in aread:
    a.append(int(i))
    pass
# print(a)
# def calculate(n):
#     while n != 1:
#         return 1
def c(i,list):
    n = 1
    if i == 0:
        return 1
    else:
        for element in list[:i]:
            n*=element
            pass
        return n

# print(c(1,[2,2,3]))
b = []
# b.append(m%c(1,a))
# print(b)
tem = 0
for i in range(n):
    b.append(int((m%c(i+1,a) - tem)/c(i,a)))
    tem = m%c(i+1,a)
    pass

ans = " ".join(map(str,b))
print(ans) # 1,2,3
