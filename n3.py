import matplotlib.pyplot as plt

# отрезок [a,b]
a = 1
b = 1.5

# шаг
h = 0.05

# начальные условия
y0 = 0
x0 = 1

# кол-во итераций
n = (b - a) / h

f = lambda x, y: x + y / x
ylist = []
xlist = []

for i in range(round(n + 1)):
    xlist.append(x0 + i * h)

print('Метод Рунге-Кутта:')
prev_y = y0
for i in range(len(xlist)):
    ylist.append(prev_y)
    print(round(prev_y, 3))
    k1 = f(xlist[i], prev_y)
    k2 = f(xlist[i] + h / 2, prev_y + (h / 2) * k1)
    k3 = f(xlist[i] + h / 2, prev_y + (h / 2) * k2)
    k4 = f(xlist[i] + h, prev_y + h * k3)
    y = prev_y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    prev_y = y


lst = []
print('Точное решение: ')
for x in xlist:
    func = x ** 2 - x
    lst.append(func)
    print(round(func, 3))


plt.rc('font', **{'family': 'verdana'})
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(xlist, ylist, "b-o", label="метод Рунге")
plt.plot(xlist, lst, "g--", label="точное решение")
plt.legend()
plt.grid()
plt.show()


