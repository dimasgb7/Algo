def solutionA(A,K):
    if not A:
        pass
    else:
        for _n in range(K):
            A = [A.pop()] + A
    
    return A

def solutionB(A,K):
    for _n in range(K):
        tmp = A[:-1]
        A = [A[len(A) -1]] + tmp

    print(A)
 
if __name__ == "__main__":
    #Test Inputs
    A = []
    K = 2

    #Solution Process
    resp = solutionA(A,K)
    print(resp)
    print("\n\n --- EXECUTION End --- \n\n")
