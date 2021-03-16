def solution(A,x):
    _vec = set(range(1,x+1))
    res = []

    for idx,el in enumerate(A):
        if el not in res and el <= x:
            res.append(el)
            if set(res) == _vec:
                return idx

def solutionB(A,x):
    _vec = set(range(1,x+1))
    res = set()
    for idx,el in enumerate(A):
        if el <= x:
            res.add(el)
        if res == _vec:
            return idx
    return -1

def solutionC(A,x):
    frog, leaves = 0, [False] * (x)
    
    for idx, el in enumerate(A):
        if el <= x:
            leaves[el - 1] = True
        while leaves[frog]:
            frog += 1
            if frog == x: return minute
    return -1

if __name__ == "__main__":
    ## TEST CASES AND INPUTS
    A = [1,3,1,4,2,3,5]
    B = [4,5,5,1]
    C = [1,1,1,1,1]
    x = 1

    ## RUN
    pos = solutionB(C,x)

    print("Tempo gasto para travessia:",pos)
    ## EXECUTION END
    print("\n\n -- Execution End --- \n\n")
