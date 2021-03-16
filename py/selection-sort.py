## Pratica de Algoritimos em Python 
## 
## Autor:Dimas Germano Brandão Soares Silva
##
## Titulo: 
## Descrição:


#   [Selection Sort]
#
def solution(seq):
    newSeq = []
    n = len(seq)

    _min = seq[0]
    

    for _ in range(n):
        _min = seq[0]
        key = 0
        for idx,el in enumerate(seq):
            if el < _min:
                _min = el
                key = idx
       
        newSeq.append(_min)
        del seq[key] 

    return newSeq

if __name__ == "__main__":
    ## Casos de Teste
    A = [8,5,9,3,6]
    B = [6,6,6,6,6]
    C = [0]
    D = [7,7,7,7,6]
    E = [11111,2222222222,333333333333,5555555555,66666666666]
    F = [-1,-3,-7,-5,-4]
    
    TESTE_VEC = (A,B,C,D,E,F)

    ## Exec
    for teste in TESTE_VEC:
        print("Sequencia a ser ordenada:",teste)
        ss = solution(teste)
        print(ss)
   



    ## FIM DA EXECUCAO
    print("\n\n -- Execution End --- \n\n")
