import numpy as np 
import matplotlib.pyplot as plt 

P=np.array([1,2])
n1=np.array([1,-1]) # normal vector of line (1,-1)X + 2 = 0
n2=np.array([7,-1]) # normal vector of line (7,-1)X + 3 = 0

N_1=n1/(np.linalg.norm(n1)) # unit vector along n1
N_2=n2/(np.linalg.norm(n2)) # unit vector along n2

D_1=N_1+N_2
D_2=N_2-N_1

def intersection_with_y_axis(point,normal): #this function returns y intercept of a line if given a point passing through it and its normal vector
	return ((np.matmul(normal.T,point))/normal[1])

# Y_1 be the point where diagonal along D_1 intersects y-axis
Y_1=np.array([0,intersection_with_y_axis(P,D_2)])	

# Y_2 be the point where diagonal along D_2 intersects y-axis
Y_2=np.array([0,intersection_with_y_axis(P,D_1)])	

plt.xlim(0, 3), plt.ylim(0, 3)
plt.plot([P[0],Y_1[0],3],[P[1],Y_1[1],1],color='r',label='Diagonal along D_1')
plt.plot([P[0],Y_2[0],3],[P[1],Y_2[1],6],color='b',label='Diagonal along D_2')
plt.text(1,2.1,'P')
plt.plot(1,2,'o')
plt.legend()
plt.grid()

plt.show()
