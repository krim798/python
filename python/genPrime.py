#prime numbers
# def genPrimes():
#     yield 2
#     primes=[2]
#     number=3
#     while True:
#         for p in primes:
#             if number%p==0:
#                 break
#         else:
#             primes.append(number)
#             yield number
#         number+=2

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
def print_prime_numbers(n):
    generator = genPrimes()
    for _ in range(n):
        print(next(generator))

print_prime_numbers(10)