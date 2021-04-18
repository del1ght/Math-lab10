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


# Euler
prev_y = y0
print('Метод Эйлера:')
for i in range(len(xlist)):
    ylist.append(prev_y)
    print(round(prev_y, 3))
    y = prev_y + h * f(xlist[i], prev_y)
    prev_y = y


# массив с точными значениями
lst = []
print('Точное решение: ')
for x in xlist:
    func = x ** 2 - x
    lst.append(func)
    print(round(func, 2))

plt.rc('font', **{'family': 'verdana'})
plt.xlabel("ось абцисс")
plt.ylabel("ось ординат")
plt.plot(xlist, ylist, "b-o", label="метод Эйлера")
plt.plot(xlist, lst, "g--", label="точное решение")
plt.legend()
plt.grid()
plt.show()