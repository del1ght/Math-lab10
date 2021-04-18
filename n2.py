import matplotlib.pyplot as plt

# отрезок [a,b]
a = 0
b = 0.5

# шаг
h = 0.05

# начальные условия
y0 = 1
x0 = 0

# кол-во итераций
n = (b - a) / h

f = lambda x, y: -(x * y) / (1 + x ** 2)
ylist = []
xlist = []
acc_ylist = []
for i in range(round(n + 1)):
    xlist.append(x0 + i * h)

print(xlist)

# Euler
prev_y = y0
tmp_x = x0
prev_accy = y0
print('Метод Эйлера-Коши:')
for i in range(len(xlist)):
    ylist.append(prev_y)
    acc_ylist.append(prev_accy)
    print(round(prev_accy, 3))
    y = prev_y + h * f(tmp_x, prev_y)
    acc_y = prev_accy + h * (f(tmp_x, prev_accy) + f(tmp_x + h, y)) / 2
    tmp_x += h
    prev_accy = acc_y
    prev_y = y


# массив с точными значениями
lst = []
print('Точное решение: ')
for x in xlist:
    func = (1 + x ** 2) ** (-1 / 2)
    lst.append(func)
    print(round(func, 3))

plt.rc('font', **{'family': 'verdana'})
plt.xlabel("ось абцисс")
plt.ylabel("ось ординат")
plt.plot(xlist, acc_ylist, "r-o", label="точное приближение")
plt.plot(xlist, lst, "g--", label="точное решение")
plt.plot(xlist, ylist, "r-o", label="нулевое приближение")
plt.legend()
plt.grid()
plt.show()
