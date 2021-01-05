from lib.factors import get_factors

answer  = []
current = 1000

while current < 9877:
    factors = get_factors(current)
    
    # Skip primes and [1, sqrt(x), x]
    if len(factors) < 4:
        current += 1
        continue

    factors = factors[1:-1]
    lowers  = factors[:len(factors)//2]
    uppers  = factors[len(factors)//2 + (0 if len(factors) % 2 == 0 else 1):][::-1]

    current_list = [int(i) for i in str(current)]
    checker_base = [i for i in range(1,10) if i not in current_list]

    valid = False


    # Check factor pairs
    for key, lower in enumerate(lowers):
        checker = checker_base.copy()
        upper = uppers[key]

        lower_list = [int(i) for i in str(lower)]
        upper_list = [int(i) for i in str(upper)]
        
        if all(x in checker for x in lower_list):
            checker = [i for i in checker if i not in lower_list]
        else:
            continue

        if all(x in checker for x in upper_list):
            checker = [i for i in checker if i not in upper_list]
        else:
            continue

        if len(checker) == 0:
            valid = True
            break


    if valid:
        answer.append(current)

    current += 1


print(sum(answer))