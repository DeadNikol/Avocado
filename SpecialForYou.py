def From10(x,q):
    x = int(x)
    q = int(q)
    y = list(range(100))
    z = list()
    p = ''
    for i in range(len(y)):
        if x / q >= 1:
            z.append(x % q)
            x = x // q
        else:
            z.append(x % q)
            z.reverse()
            for i in range(len(z)):
                if z[i] == 10:
                    z[i] = 'A'
                elif z[i] == 11:
                    z[i] = 'B'
                elif z[i] == 12:
                    z[i] = 'C'
                elif z[i] == 13:
                    z[i] = 'D'
                elif z[i] == 14:
                    z[i] = 'E'
                elif z[i] == 15:
                    z[i] = 'F'
            for i in range(len(z)):
                z[i] = str(z[i])
                p += z[i]
            return (p)
            break

def To10(x,y):
    p = 0
    x = list(x)
    y = int(y)
    z = list()
    x.reverse()
    for i in range(len(x)):
        if x[i]=='A':
            x[i]=10
        if x[i]=='B':
            x[i]=11
        if x[i]=='C':
            x[i]=12
        if x[i]=='D':
            x[i]=13
        if x[i]=='E':
            x[i]=14
        if x[i]=='F':
            x[i]=15
    for i in range(len(x)):
        z.append(int(x[i])*y**i)
    for i in range(len(z)):
        p += int(z[i])
    return(p)

x = input('Введите число: ')
y = int(input('Введите начальную систему: '))
z = int(input('Введите конечную систему: '))
if y == 10:
    print(From10(x, z))
else:
    a = int(To10(x, y))
    b = From10(a, z)
    print((b))
