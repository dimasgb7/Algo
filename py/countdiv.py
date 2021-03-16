## Pratica de Algoritimos em Python 
## 
## Autor:Dimas Germano Brandão Soares Silva
##
## Titulo: 
## Descrição:


#   [Count Div]
#
def solution(A,B,K):
    
    cnt = 0
    _vec = [A] if A == B else range(A,B)

    for el in _vec:
        if el%K == 0:
            cnt +=1

    return cnt 

if __name__ == "__main__":
    ## Casos de Teste
    '''
    A,B,K = 11,345,17
    ss = solution(A,B,K)
    print(ss)
    A,B,K = 6,11,2
    ss = solution(A,B,K)
    print(ss)
    
    '''
    A,B,K = 1,1,11
    ss = solution(A,B,K)
    print(ss)



    

    ## FIM DA EXECUCAO
    print("\n\n -- Execution End --- \n\n")
