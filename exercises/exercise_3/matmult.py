# Program to multiply two matrices using nested loops
import random
import numpy as np

@profile
def main():
    N = 250 
    
    # NxN matrix
    X = []
    np.random.seed(10)
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    
    # Nx(N+1) matrix
    Y = []
    np.random.seed(20)
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
                
    for r in result:
        print(r)
    return result

@profile
def optimized():
    N = 250
    
    # Random matrices
    X = np.random.randint(0, 100, size = [N, N])
    Y = np.random.randint(0, 100, size = [N, N])
    
    # Matrix multiplication
    result_opt = np.matmul(X, Y)
    return result_opt

if __name__ == '__main__':
    result = main()
    result_opt = optimized()
    
    