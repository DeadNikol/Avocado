import Nepolicarbonat
import Policarbonat
x = int(input('1 если из 10 в x, 2 если из x в 10: '))
if x == 1:
    Policarbonat.From10()
elif x == 2:
    Nepolicarbonat.To10()
else:
    print("Пошёл нахер, нет такого функционала")