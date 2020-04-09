#===========================================================================
#                           GENERATORS Module
#===========================================================================
"""
# Presents generators (introduced by PEP 255)
#
# Generators :
#   - are iterables defined by functions
#   - are lazy iterators, on evry cycle a single output
#   - generate sequences with no defined end
#   - must include 'yield' (once at least), may use return (as flow control)
#
# It should be noticed that each call to a generator creates a difefrent object
#   which I call here iterator. This means that we can run thru same genrator
#   in parallel without having inter-iterators effects
#
# Generators are a great mean to be ued on very long or endless process:
#   Sesnors reading
#   Somputational Step
#   Huge file reading (chunl at a time)
#
# Author: Shuky Persky
#
"""

#===========================================================================
# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def isprime(n):
    '''check if integer n is a prime
    :returns: bool  True - number is a prime
                    False- number isn't a prime
    :raises: TypeError
    '''
    # make sure n is a positive integer

    try:
        n = abs(int(n))

    except TypeError as T_e:
        raise ValueError(f'Type Err: {V_e!r}')

    except Exception as e:
        raise Exception(f'Soem Err: {e!r}')

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False

    return True


# ===========================================================================
def fibo(max_val):
    ''' Calculutes the Fibonacci Sequence members
    To avoid endless running
    :args:      max_val(int)
    :yields:    (int)
    '''

    a = 0
    b = 1
    while (True):
        yield (a+b)
        a, b = b, b+a
        if ((a+b) > max_val):
            break

# ===========================================================================
def squares_func(nums):
    result = []
    for num in nums:
        result.append(num*num)
    return result

def squares_gnrtr (nums):
    for num in nums:
        yield (num * num)


#===========================================================================
def simple_gnrtr_abc():
    print('\n generates a')
    yield 'a'
    print('\n generates b')
    yield 'b'
    print('\n generates c')
    yield 'c'


#===========================================================================
#def take(count, iterable):
#    counter = 0




#===========================================================================
def generators_mdl():
    '''
    #module entry point function
    Args-name(type) none
    :return(type)   none
    '''

    print ('\n\n ======== Generators Module is Running ')


    #prepare input
    nums = [1, 2, 3, 4, 5, 6]   #

    # ---------------------------------------------------------------------------
    # Simple case - create a generator iterator
    # ---------------------------------------------------------------------------
    #fibo
    for num in fibo(100):
        print(num)

    #simple generator
    g =  simple_gnrtr_abc() #instantiate a generator. It is like an iterator
    next(g)     # 'a'
    next(g)     # 'b'
    next(g)     # 'c'

    # ---------------------------------------------------------------------------
    #   Other mechanisms: functions, comprehesion
    # ---------------------------------------------------------------------------
    #call a function
    squres_from_func = squares_func (nums)
    print('\n Squares from function: {0}'.format(squres_from_func ))

    #Use comprehnsion
    squares_from_comprehesion = [x*x for x in nums]
    print ('\n Squares from comprehension: {0}'.format(squares_from_comprehesion))

    # ---------------------------------------------------------------------------
    #   calling a function vs. calling a ggenerator
    # ---------------------------------------------------------------------------
    #(1) trigger the generator & call it in loop control
    squares_from_gnrtr = []
    squares_gnrtr_hndlr = squares_gnrtr (nums)
    for square in squares_gnrtr_hndlr:
        squares_from_gnrtr.append(square)
    print('\n [1] Squares / calls to generator by ''calling'' the handler: {0}'.format(squares_from_gnrtr ))

    #(2) trigger the generator & call it in loop control
    squares_from_gnrtr = []
    for square in squares_gnrtr (nums):
        squares_from_gnrtr.append(square)
    print('\n [2] Squares / calls to generator by ''calling'' the handler: {0}'.format(squares_from_gnrtr ))

    #trigger the generator & call it from loop logic using 'next()'
    squares_from_gnrtr = []
    squares_gnrtr_iterator = squares_gnrtr(nums)
    for num in nums:
        squares_from_gnrtr.append(next(squares_gnrtr_iterator))
    print('\n [3] Squares / calls to generator by using next(): {0}'.format(squares_from_gnrtr ))

    # ---------------------------------------------------------------------------
    #   Generator Expression
    # ---------------------------------------------------------------------------
    print('\n\n Generator Expression \n')
    many_squares = (x*x for x in range(1, 10))     # create generator object
    print('SUM of all values: {0}'.format(sum(many_squares)))
    prime_squares = (x * x for x in range (1, 10) if isprime(x))
    print ('SUM of prime values: {0}'.format (sum (prime_squares )))

    #itertools services: count, islice
    from itertools import count, islice
    print('\nitertools: ')
    some_primes = islice((1.7*x for x in count()), 10)  # slice of 10 values
    print('\n', list(some_primes)[-4:])

    #itertools services: any, all
    x = any (((x % 3) == 0) for x in range (1, 43))                     #true if there is at least single true
    print (f'\n [1] x={x}')
    x = all (((x % 3) == 0) for x in range (1, 43))                     #true if all are true
    print (f'\n [2] x={x}')
    x = all (((x % 3) == 0) for x in range (1, 43) if ((x % 3) == 0))   #true if all are true
    print (f'\n [3] x={x}')


    print ('\n ----------- Generators Module is Done >>>> ')


