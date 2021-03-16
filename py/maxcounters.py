## Pratica de Algoritimos em Python 
## 
## Autor:Dimas Germano Brandão Soares Silva
##
## Titulo: Max Counters
## Descrição:
##      Encontrar o vetor de contagem final dado que um array de operações modifica 
##      o vetor inicial até seu estado final.


def max_counter(x):
    if x.count(x[0]) == len(x):
        return [max(x)] * len(x)
    
    return x

#   [Max_Counters]
#   Usando 2 variaveis auxiliares para otimizar a execução, _max guarda o valor do 
#   ultimo maximo encontrado durante a operação. A flag _double_max garante que não 
#   ocorram duas operações de maximizar os contadores seguidas.
#
def solution(A,N):
    my_cnt = [0]*N
    
    _max = 0
    _double_max = False
    for el in A:
        if 1 <= el <=N:
            my_cnt[el-1] += 1
            _double_max = False

            if my_cnt[el-1] > _max:
                _max = my_cnt[el-1]

        elif el > N and not _double_max:
            my_cnt = [_max] * N
            _double_max = True
        

    return my_cnt
    
   

if __name__ == "__main__":
    ## Casos de Teste
    A = [6]*1000000000
    B = [3,4,4,6,1,4,4]
    
    N = 5

    ## Exec
    ss = solution(A,N)
    print("Array final:",ss)
    ss = solution(B,N)
    print("Array final:",ss)

    ## FIM DA EXECUCAO
    print("\n\n -- Execution End --- \n\n")
