n = int(input())
#year
y = n//365
#week
w = (n%365)//7
#days
d = (n%52)//7

print(y,w,d)
