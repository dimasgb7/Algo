def solutionA(X, Y, D):
    '''
    O problema dessa solução é a complexidade necessaria para calcular o resultado.
    A complexidade vai depender do valor de D, assim podendo ser O(N) ou O(N2) ou pior
    '''
    pos = X
    cnt = 0

    while pos < Y:
        cnt = cnt + 1
        pos = pos + D
    
    print("-- End position:", pos)
    print("-- Number of jumps:", cnt)
    
    return pos

def solutionB(X, Y, D):
    tmp = ((Y - X)/D)
    '''
    if( tmp - int(tmp) > 0 ):
        n_jmp = int(tmp) + 1
    '''
    n_jmp = int(tmp) + int( (tmp - int(tmp) > 0) )

    print("-- End position:", (n_jmp*D) + X)
    print("-- Number of jumps:", n_jmp)
    
    return n_jmp

if __name__ == "__main__":
    ## TEST CASES AND INPUTS
    X = 10
    Y = 85
    D = 30

    ## RUN
    solutionB(X,Y,D)

    ## EXECUTION END
    print("\n\n -- Execution End --- \n\n")
