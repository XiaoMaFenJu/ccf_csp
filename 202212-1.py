n,i = input().split()
income_r = input().split()

n = int(n)
i = float(i)

income = []
for elements in income_r:
    income.append(int(elements))
    pass

# print(income)
money = 0

for t in range(n+1):
    # print(t)
    money += income[t] * (1 + i)**(n-t)
    pass

money = money/(1+i)**n

print(money)