import numpy as np
import time

start_time = time.time()

rings = []
def get_rings(matrix):
    order = matrix.shape[0]
    num_rings = order // 2
    
    for i in range(1,num_rings):
        ring_name = f'ring_{i + 1}'
        ring = np.concatenate((matrix[i, i:-i], matrix[i+1: -i,-i-1], np.flip(matrix[- i - 1, i:-i-1]), np.flip(matrix[i+1:-i-1, i])))
        rings.append(ring)
    
    return rings

def reconstruct_matrix(rings,n):
    matrix = np.zeros((n, n), dtype=int) 
    matrix[0][0:n]=rings[0][0:n]
    matrix[1:,-1]=rings[0][n:2*n-1]
    matrix[-1,:-1]=np.flip(rings[0][2*n-1:3*n-2])
    matrix[1:-1,0]=np.flip(rings[0][3*n-2:4*n-4])
    
    for i in range(1,n//2):
        matrix[i, i:-i]         =   rings[i][0              : (n-2)-2*(i-1)]
        matrix[i+1: -i,-i-1]    =   rings[i][(n-2)-2*(i-1)      : 2*((n-2)-2*(i-1))-1]
        matrix[- i - 1, i:-i-1] =   np.flip(rings[i][2*((n-2)-2*(i-1))-1: 3*((n-2)-2*(i-1))-2])
        matrix[i+1:-i-1, i]     =   np.flip(rings[i][3*((n-2)-2*(i-1))-2: 4*((n-2)-2*(i-1))-4])
    
    return matrix


def check_magic_square(matrix):
    reference_sum = np.sum(matrix[0, :])
    
    for row in matrix:
        if np.sum(row) != reference_sum:
            return False
    
    for col in matrix.T:  
        if np.sum(col) != reference_sum:
            return False
    
    if np.sum(np.diag(matrix)) != reference_sum:
        return False
    
    if np.sum(np.diag(np.fliplr(matrix))) != reference_sum:
        return False
    
    return reference_sum, matrix

                    
def rotate_me8(rings):
    for i in range (len(rings[0])):
        rings[0]=np.roll(rings[0],1)
        for j in range (len(rings[1])):
            rings[1]=np.roll(rings[1],1)
            for k in range (len(rings[2])):
                rings[2]=np.roll(rings[2],1)
                d=check_magic_square(reconstruct_matrix(rings,8))
                if (d!=False):
                    return(d)

def rotate_me6(rings):
    for i in range (len(rings[0])):
        rings[0]=np.roll(rings[0],1)
        for j in range (len(rings[1])):
            rings[1]=np.roll(rings[1],1)
            
            d=check_magic_square(reconstruct_matrix(rings,6))
            if (d!=False):
                return(d)
 

if __name__ == "__main__":
    order = int(input())
    
    # Get elements
    elements = list(map(int, input().split()))

    # Reshape the elements into a square matrix
    matrix = np.array(elements).reshape(order, order)

    rings.append(np.concatenate((matrix[0,:], matrix[1:,-1], np.flip(matrix[-1,:-1]),np.flip(matrix[1:-1,0]))))
    rings = get_rings(matrix)

    if order==8:
        print(rotate_me8(rings))
    elif order==6:
        print(rotate_me6(rings))


