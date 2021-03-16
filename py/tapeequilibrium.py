def solutionA(A):
    split_points = range(1,len(A)) 
    diff = []

    for a in split_points:
        A_a = A[:a]
        A_b = A[a:]

        diff.append(abs(sum(A_a) - sum(A_b)))
    
    return min(diff)

def solutionB(A):
    low = []
    high = []
    for idx in range(len(A) - 1):
        tmp = low[idx - 1] if low else 0
        low.append(A[idx] + tmp)
        
        tmp2 = high[idx - 1] if high else 0
        high.append(A[-idx-1] + tmp2)

    high = list(reversed(high)) 
    
    '''
    hold = abs(low[0] - high[0])
    for idx in range(1,len(A) - 1):
        tmp = abs(low[idx] - high[idx])
        hold = tmp if tmp<hold else tmp
    
    diff = min([ abs(low[idx] - high[idx]) for idx in range(len(A)-1) ])
    '''
    '''
    for idx,(a,b) in enumerate(zip(low,high)):
        tmp = abs(a-b)
        if idx > 0:
            hold = tmp if tmp < hold else hold
        else:
            hold = tmp
    '''
    
    diff = min([ abs(a-b) for a,b in zip(low,high)])
    print(low)
    print(high)
    print(diff)
    return hold

if __name__ == "__main__":
    ## TEST CASES AND INPUTS
    A = [3,1,2,4,3]
    ## RUN
    res = solutionB(A)
    print("Menor diferença encontrada:",res)

    ## EXECUTION END
    print("\n\n -- Execution End --- \n\n")
