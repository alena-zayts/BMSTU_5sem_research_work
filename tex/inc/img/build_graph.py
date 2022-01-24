import matplotlib.pyplot as plt

x = list(range(2010, 2020))
y = [280, 290, 370, 440, 520, 500, 670, 580, 725, 795]

plt.figure(figsize=(7,5))
plt.xticks(list(range(2009, 2021)))
plt.yticks(list(range(0, 1000, 100)))
plt.xlim([2009, 2020])
plt.ylim([0, 1000])
plt.grid(True)

plt.xlabel('Год')
plt.ylabel('Количество статей')

plt.plot(x, y)
plt.scatter(x, y, color='blue', marker='.')
plt.show()
