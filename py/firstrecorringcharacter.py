## Pratica de Algoritimos em Python 
## 
## Autor:Dimas Germano Brandão Soares Silva
##

## Titulo: First Recurring Character

#Caso1: Retornar o caracter que se repete, seguindo a ordem como prioridade de seleção
def solution(A):
    
    _dict = {}

    for el in A:
        if el not in _dict.keys():
            _dict[el] = 1
        else:
            _dict[el] += 1

    for _key in _dict.keys():
        if _dict[_key] > 1:
            return _key
    
    return None

# Caso 2: Retornar o primeiro caracter a se repetir
def solutionB(A):
    
    _dict = {}

    for el in A:
        if el not in _dict.keys():
            _dict[el] = 1
        else:
            return el
    return None   

if __name__ == "__main__":
    ## Casos de Teste
    A = ['A','B','C','B']
    B = ['B','C','A','C','B','A']
    C = ['A','B','C']

    ## Exec
    ss = solution(A)
    print(ss)
    bb = solution(B)
    print(bb)
    cc = solution(C)
    print(cc)
    ## FIM DA EXECUCAO
    print("\n\n -- Execution End --- \n\n")
