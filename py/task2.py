## Pratica de Algoritimos em Python 
## 
## Autor:Dimas Germano Brandão Soares Silva
##
## Titulo: 
## Descrição:


#   [Missing Integers]
#
def solution(S,N):
    _dic = {}
    reserv = S.split(" ")
    if S == '':
        return N*3

    for _n in range(N):
        _dic[_n+1] = [0]*10
    
    
    for el in reserv:
        row = int(el[0])
        col = el[1]

        if col == 'A': col = 0
        elif col == 'B': col = 1
        elif col == 'C': col = 2
        elif col == 'D': col = 3
        elif col == 'E': col = 4
        elif col == 'F': col = 5
        elif col == 'G': col = 6
        elif col == 'H': col = 7
        elif col == 'J': col = 8
        elif col == 'K': col = 9

        _dic[row][col] = 1
     
    alloc = 0
    for key in _dic.keys():
        
        slice_tup = [(0,3),(3,7),(7,10)]
        for low,high in slice_tup:
            max_seq = 0
            cnt = 0
            for el in _dic[key][low:high]:
                if el == 0:
                    cnt += 1
                else:
                    if cnt > max_seq:
                        max_seq = cnt
                    cnt = 0

            max_seq = cnt if cnt > max_seq else max_seq
            alloc += max_seq // 3

    print("Alocacoes", alloc)
    print('\n\n')
        
    return alloc

if __name__ == "__main__":
    ## Casos de Teste
    S = ""
    N = 10
    
    ## Exec
    print("Vetor teste:",S)
    print("Numero de linhas:",N)
    ss = solution(S,N)
    print(ss)

    ## FIM DA EXECUCAO
    print("\n\n -- Execution End --- \n\n")
