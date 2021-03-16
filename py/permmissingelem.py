def solution(A):
    n = len(A) + 1
    t_total = (n + 1) * n // 2
    
    a_total = 0
    for el in A:
        a_total = el + a_total

    _res = t_total - a_total

    print("Numero faltando:",_res)
        

if __name__ == "__main__":
    ## TEST CASES AND INPUTS
    A = [2,3,1,4]
    B = [2] 
    C = []
    ## RUN
    solution(A)
    solution(B)
    solution(C)

    ## EXECUTION END
    print("\n\n -- Execution End --- \n\n")
