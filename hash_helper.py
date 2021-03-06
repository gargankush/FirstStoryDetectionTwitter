from fractions import gcd
import random
from constants import *

def get_sieve(N):
    prime = [1] * (N + 1)
    prime[0] = 0
    prime[1] = 0
    for i in range(N + 1):
        if prime[i]:
            for j in range(i * 2, N + 1, i):
                prime[j] = 0
    primes = []
    for i in range(N + 1):
        if prime[i]:
            primes.append(i)

    return primes

def generate_permutation_hash_functions( length, count ):
    primes = get_sieve(100000)
    next = 100
    hash_functions = []
    random.seed(5)

    # b = 523

    for x in range(count):
        while gcd(length, primes[next]) != 1:
            next += 1
        b = random.randint(0, length)
        hash_functions.append( { 'a' : primes[next] , 'b' : b })
        next += 1

    return hash_functions



# def xor_range_hasher(length):
#     curr = 1
#     while curr < length:
#         curr <<= 1
#     #partition 0 .. curr into segments
#     func = lambda x : ( x * NUM_BUCKETS ) / curr
    
#     return func

def weighted_sum_hasher(length, rowmax, count):
    hash_functions = []
    primes = get_sieve(100000)
    next = 1
    weights = []
    random.seed(13)
    for y in range(length):
        # weights.append(randint(int((rowmax * xx) / count), int((rowmax * (xx + 1)) / count)))
        weights.append(random.random())

    for xx in range(count):
        # weights = list(map(lambda x : x / float(sum(weights)), weights))
        func = lambda x : (primes[next]*(sum([x[i] * weights[i] for i in range(length)])) + 5) % NUM_BUCKETS
        next += 1
        hash_functions.append(func)
    return hash_functions

        
            
