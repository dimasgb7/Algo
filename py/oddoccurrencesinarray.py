from functools import reduce 
def solution(A):
    for el in set(A):
        if A.count(el) % 2:
            break

    print("Odd element is: {}".format(el))
    return el

def solutionB(A):
    _res = reduce( lambda x,y: x^y , A )
    print("Odd element is: {}".format(_res))
    return _res

def solutionC(A):
    _res = A[0]
    for idx in range(1,len(A)):
        _res = _res ^ A[idx] 

    print("Odd element is: {}".format(_res))
    return _res

if __name__ == "__main__":
    # TEST CASES
    ## LISTA NUNCA SERÁ VAZIA
    ## CASOS POSSIVEIS: LISTA PEQUENA, LISTA GIGANTESCA
    A = [9,3,9,3,9,7,9]
    B = [9,3,9,9,3,7,7]

    # Process
    solutionC(A)
    solutionC(B)
    print("\n\n -- Execution End --- \n\n")
