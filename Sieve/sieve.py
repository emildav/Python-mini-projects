
def sieve(n):

    raw_list = [num for num in range(2, n+1)]

    for i in range(len(raw_list)):
        if raw_list[i] == 0:
            continue
        else:
            for j in range(i + raw_list[i], len(raw_list), raw_list[i]):
                if raw_list[j] % raw_list[i] == 0:
                    raw_list[j] = 0
                else:
                    continue
    
    return [num for num in raw_list if num != 0]

print(*sieve(30))
print(*sieve(100))
