def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    参数:    N - 正整数
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    if N <= 2:
        return ""
    # 埃拉托斯特尼筛法：先初始化一个布尔数组标记是否为质数
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            # 将i的倍数标记为非质数
            is_prime[i*i : N : i] = [False] * len(is_prime[i*i : N : i])
    # 收集所有质数并转为字符串
    primes = [str(i) for i, val in enumerate(is_prime) if val]
    return ' '.join(primes)

if __name__ == "__main__":
    N = int(input().strip())
    print(PrimeList(N))

