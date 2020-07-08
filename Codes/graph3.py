import numpy as np 
import matplotlib.pyplot as plt
P=np.array([1,2])
n1=np.array([1,-1]) # normal vector of line (1,-1)X + 2 = 0
n2=np.array([7,-1]) # normal vector of line (7,-1)X + 3 = 0

N_1=n1/(np.linalg.norm(n1)) # unit vector along n1
N_2=n2/(np.linalg.norm(n2)) # unit vector along n2

D_1=N_1+N_2
D_2=N_2-N_1

def intersection_with_y_axis(point,normal):  #this function returns y intercept of a line if given a point passing through it and its normal vector
	return ((np.matmul(normal.T,point))/normal[1])

A=np.array([0,intersection_with_y_axis(P,D_2)])
 #C be the diagonally opposite point of A
C=2*P - A 	


def intersect(p1,n1,p2,n2):
	M=np.vstack((n1,n2))
	b=np.array([np.matmul(n1,p1.T),np.matmul(n2,p2.T)])
	return np.matmul(np.linalg.inv(M),b)

# B and D are remaining two points
B=intersect(A,n1,C,n2)
D=intersect(A,n2,C,n1)

len=10
lam_1=np.linspace(0,1,len)

x_AB=np.zeros((2,len))
x_BC=np.zeros((2,len))
x_CD=np.zeros((2,len))
x_AD=np.zeros((2,len))
x_BD=np.zeros((2,len))
x_AC=np.zeros((2,len))
	
for i in range(len):
	temp1=A+lam_1[i]*(B-A)
	x_AB[:,i]=temp1.T
	temp2=B + lam_1[i]*(C-B)
	x_BC[:,i]=temp2.T
	temp3=C+lam_1[i]*(D-C)
	x_CD[:,i]=temp3.T
	temp4=D+lam_1[i]*(A-D)
	x_AD[:,i]=temp4.T
	temp5=D+lam_1[i]*(B-D)
	x_BD[:,i]=temp5.T
	temp6=A+lam_1[i]*(C-A)
	x_AC[:,i]=temp6.T	

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')		
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')

plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1+0.1),A[1]*(1-0.1),'A')

plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1-0.05),B[1]*(1),'B')

plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1+0.03),C[1]*(1-0.1),'C')

plt.plot(D[0],D[1],'o')
plt.text(D[0]*(1+0.05),D[1]*(1-0.1),'D')

plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1-0.03),P[1]*(1-0.2),'P')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title("Rhombus ABCD")

plt.legend(loc='best')
plt.grid()
plt.show()

