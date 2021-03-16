## Pratica de Algoritimos em Python 
## 
## Autor:Dimas Germano Brandão Soares Silva
##
## Titulo: 
## Descrição:


#   [Missing Integers]
#
def solution(A):
    _base = 0
    _max = 0
    _A = list(set(A))
    
    for idx in range(1,len(_A)):
        chk = _A[idx] == _A[idx-1]+1
        if _A[idx] == _A[idx-1] + 1:
            continue
        _res = _A[idx-1]+1
        return _res if _res > 0 else 1 
     
    return _A[-1] + 1
    


if __name__ == "__main__":
    ## Casos de Teste
    A = [1,3,6,4,1,2]
    B = [-1,-3]
    C = [1,2,3] 
    D = [2,5,6,7,8]
    ## Exec
    ss = solution(A)
    print(ss) 
    bb = solution(B)
    print(bb)
    cc = solution(C)
    print(cc)
    dd = solution(D)
    print(dd)
    ## FIM DA EXECUCAO
    print("\n\n -- Execution End --- \n\n")
