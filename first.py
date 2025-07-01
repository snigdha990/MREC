s=[1,2,3,4,1,2,3,4,5]
n=len(s)
max=s[0]
for i in range(n):
    if s[i]>max:
        max=s[i]
print(max)
 