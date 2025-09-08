L = list(map(int,input().split()))

s = sum(L)
a = avg(L)
p = (s//len(L))*100

print("sum",s)
print("average",a)
print("percent",p)
