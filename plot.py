import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

def plot_sine(n_x = 21, n_y = 21):	
	nx, ny = (n_x, n_y)
	x = np.linspace(0, 1, nx)
	y = np.linspace(0, 1, ny)
	xv, yv = np.meshgrid(x, y)
	zv = np.sin((xv + yv)*np.pi)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')
	ax.plot_trisurf(xv.flatten(), yv.flatten(), zv.flatten(), cmap = 'jet')
	plt.show()

plot_sine(64, 64)
