def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔
    参数：N - 正整数
    返回：str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    if N <= 2:
        return ""
    primes = []
    for num in range(2, N):  # 从2开始，因为1不是质数
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    return ' '.join(primes)

if __name__ == "__main__":
    N = int(input().strip())  # 添加int转换和strip处理
    result = PrimeList(N)
    print(result)
   
    x = PrimeList(10000)
    print(x)
