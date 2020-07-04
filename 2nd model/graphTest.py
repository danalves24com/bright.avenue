import matplotlib.pyplot as plt
data = [[1,2],[2,4]]
x = []
y = []
for ar in data:
    x.append(ar[0])
    y.append(ar[1]) 
    print(ar[0], ar[1])
plt.plot(x, y)
plt.show()