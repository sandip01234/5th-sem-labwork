import collections

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def etf(m):
    unique_factors = set(prime_factors(m))
    result = m
    for p in unique_factors:
        result *= (p - 1)
        result //= p
    return result

def main():
    a = 5
    m = 12
    etf_ = etf(m)
    
    print("Φ(m):", etf_)

    if pow(a, etf_, m) == 1:
        print("Thus", etf_,"Number are Relatively Prime to", m)
    else:
        print("Thus", etf_,"Number are not Relatively Prime to", m)
main()
