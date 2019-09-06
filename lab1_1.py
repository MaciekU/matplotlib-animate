import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time
from random import randint
import matplotlib.animation as animation

def generate_integer(L):
    for i in range(L):
        yield randint(0,100)

generator = generate_integer(100)

# slow print
def slow_print():
	fig = plt.figure()
	numbers = []
	plt.show(block=False)

	for i in range(100):
		numbers.append(next(generator))
		# time.sleep(0.01)
		plt.hist(numbers, bins=[x for x in range(0,100)], normed=1)
		for i in numbers:
		    print(i)
		
		fig.canvas.draw()
		print("rys")

# faster
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
numbers = []

def animate(i):
	numbers.append(next(generator))
	ax1.clear()
	plt.hist(numbers, bins=[x for x in range(0,100)], normed=1)

def fast_print():
	# interval in ms
	ani = animation.FuncAnimation( fig, animate, interval = 30)
	plt.show()

fast_print()




