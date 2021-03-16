## Pratica de Algoritimos em Python 
## 
## Autor:Dimas Germano Brandão Soares Silva
##
## Titulo: 
## Descrição:


#   [Maximum double Slice]
#
def solution(A):
    
    low = [0] * len(A)
    high = [0] * len(A)

    for i in range(1,len(A)-1):
        low[i] = max(low[i-1] + A[i],0)

    for i in range(len(A)-2, 1):
        high[i] = max(high[i+1] + A[i],0)

    _max = 0
    
    for i in range( 1, len(A) - 1):
        _max = max(_max , low[i-1] + high[i+1])

    return _max

        


   

if __name__ == "__main__":
    ## Casos de Teste
    A = [3,2,6,-1,4,5,-1,2]

    ## Exec
    ss = solution(A)
    print(ss)

    ## FIM DA EXECUCAO
    print("\n\n -- Execution End --- \n\n")
