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
        for i in range(len(z)):
            if z[i]==10:
                z[i]='A'
            elif z[i]==11:
                z[i]='B'
            elif z[i]==12:
                z[i]='C'
            elif z[i]==13:
                z[i]='D'
            elif z[i]==14:
                z[i]='E'
            elif z[i]==15:
                z[i]='F'
        print(z)
        break
