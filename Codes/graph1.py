import matplotlib.pyplot as plt 

plt.plot([-2,0,2],[0,2,0],[-2,0,2],[0,-2,0],color='b')
plt.plot([0,0],[2,-2],[-2,2],[0,0],color='b')


ax = plt.axes()
ax.arrow(0, 0, 0.9, 0.9, head_width=0.1, head_length=0.1, fc='k', ec='k')
ax.arrow(0, 0, -0.9, 0.9, head_width=0.1, head_length=0.1, fc='k', ec='k')
ax.arrow(0, 0, 0, 0.9, head_width=0.1, head_length=0.1, fc='k', ec='k')
ax.arrow(0, 0, 0.9, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
plt.title("Vector Addition")
plt.grid()
plt.show()
