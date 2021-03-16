## Pratica de Algoritimos em Python 
## 
## Autor:Dimas Germano Brandão Soares Silva
##
## Titulo: 
## Descrição:


#   [Binary Search]
#   Complexity: O(log n)
def solution(vector,target):
    low = 0
    high = len(vector) - 1

    while low <= high:
        mid = high + low//2
        if vector[mid] == target:
            return mid

        elif target < vector[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    ## Casos de Teste
    A = [1,2,3,4,5,6,7,8,9,10]
    T = 9
    ## Exec

    ss = solution(A,T)
    
    print("Vetor de entrada:", A)
    print("Objeto buscado:",T)
    print("Objeto na posição:",ss)

    ## FIM DA EXECUCAO
    print("\n\n -- Execution End --- \n\n")
