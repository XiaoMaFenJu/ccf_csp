# n<15 暴力解法
n,x = input().split()
n = int(n)
x = int(x)

pricelist = []
for i in range(n):
    pricelist.append(int(input()))
    pass
# print(pricelist)

pricelist.sort()
# print(pricelist)

cost = pricelist
min_cost = n*x

for ele in pricelist:
    temp = set()
    if not cost:
        cost.append(ele)
        continue
    for i in pricelist:
        c = ele + i
        if c < x:
            temp.add(c)
            continue
        else:
            min_cost = min(min_cost,c)
            break
    for k in temp:
        cost.append(k)
        pass
    cost.sort()
print(min_cost)