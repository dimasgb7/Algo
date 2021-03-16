## Pratica de Algoritimos em Python 
## 
## Autor:Dimas Germano Brandão Soares Silva
##
## Titulo: 
## Descrição:


#   [Missing Integers]
#
def solution(A):
    n = len(A)
    cnt = 2

    # Todos os numeros iguais ou vetor unitario 
    if n == 1 or (A.count(A[0]) == len(A)):
        return 1
    

    for i in range(n-1):
        if A[i] != A[i+1]:
            base = 1 if A[i+1] > A[i] else 0
            break

    for i in range(n-1):
        if base:
            if A[i] > A[i+1]:
                cnt +=1
                base = 0
        elif A[i] < A[i + 1]:
            cnt += 1
            base = 1
    return cnt
            

if __name__ == "__main__":
    ## Casos de Teste
    A = [2,2,3,4,3,3,2,2,1,1,2,5]
    B = [1,1,1]
    C = [-1]
    TEST_CASES = (A,B,C)
    ## Exec
    for TEST in TEST_CASES:
        print("Vetor teste",TEST)
        ss = solution(TEST)
        print(ss)

    ## FIM DA EXECUCAO
    print("\n\n -- Execution End --- \n\n")
