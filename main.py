x = int(input())
q=int(input())
y=list(range(100))
z=list()
for i in range(len(y)):
    if x/q>=1:
        z.append(x%q)
        x=x//q
    else:
        z.append(x%q)
        z.reverse()
        print(z)
        break