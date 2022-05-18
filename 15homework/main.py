def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False
def prime_list(lst):
    return [lst[n] for n in range(len(lst)) if is_prime(n)]

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(prime_list(l))