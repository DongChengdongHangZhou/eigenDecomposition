from numpy.linalg import eig
import numpy as np
import math
D = np.array([[  0,   1, 1,  1],
     [  1,   0,  math.sqrt(2) ,  math.sqrt(2)],
       [ 1,   math.sqrt(2),  0,   2],
       [ 1,  math.sqrt(2),   2,   0]])





M = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        M[i][j] = (D[0][j]*D[0][j]+D[i][0]*D[i][0]-D[i][j]*D[i][j])*0.5

print(M)

vals, vecs = eig(M)
print(vecs)

Lambda = np.diag(vals)
print(Lambda)
print(np.dot(np.dot(vecs, Lambda), vecs.T))

print(np.dot(vecs,np.sqrt(Lambda)))