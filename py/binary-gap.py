def solution(N):
    
    to_bin = lambda x : list(reversed([str((x >> i) & 1) for i in range(32)]))
    print(to_bin(N))
    
    tmp = to_bin(N)
    
    one_pos = []
    for count, value in enumerate(tmp):
        if value == "1":
            one_pos.append(count)
    BGs = [0]
    for idx in range(len(one_pos) -1):
       BGs.append(one_pos[idx+1] - one_pos[idx] - 1)
    
    return max(BGs)


if __name__ == "__main__":
    N = 1041
    res = solution(N)
    print("\nO maior binary gap será: {}\n".format(res))
    
    print("\n\n --- Execution End ---\n\n")
