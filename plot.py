import matplotlib.pyplot as plt
x = []
y = []
with open("benchmark.dat") as f:
	for line in f:
		splitted = line.split(',')
		x.append(int(splitted[0]))
		y.append(float(splitted[1]))
print x
print y
plt.plot(x,y)
plt.show()

