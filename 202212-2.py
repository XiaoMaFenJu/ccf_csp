a1,a2 = input().split()
n = int(a1)
m = int(a2)

a3 = input().split()
p = []
for i in range(m):
    p.append(int(a3[i]))
    pass

a4 = input().split()
t = []
for i in range(m):
    t.append(int(a4[i]))
    pass

######################################

def cal_t(i,p,t):
    if p[i] == 0:
        return 1
    else:
        return t[p[i]- 1] + cal_t(p[i]-1,p,t)
        pass
    pass

result = []
for i in range(m):
    result.append(cal_t(i,p,t))
    pass

ans = " ".join(map(str,result))
print(ans)

okornot = 0
for i in range(m):
    if result[i] + t[i] - 1> n:
        okornot = 1
        break
        pass
    pass

if okornot == 0:
    last = []
    for i in range(m):
        last.append(n - t[i] + 1)
        pass

    ans1 = " ".join(map(str, last))
    print(ans1)