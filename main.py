def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    参数:    N - 正整数
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    primes = []
    for num in range(2, N):  # 质数从2开始判断，遍历到N-1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # 只需判断到num的平方根
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return ' '.join(primes)
