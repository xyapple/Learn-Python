num = int(input('please enter a number'))

def prime_numer_test():

    total = 0
    factors = range(1, num)
    cfactors = range(1, num + 1)

    if num <= 1:
        print('{0:d} is not a prime'.format(num))
    elif num == 2:
        print('{0:d} is a prime number'.format(num))
    elif num % 2 == 0:
        print('{0:d} is NOT a prime number'.format(num))
    else:
        for i in cfactors:
            if (num % i ) == 0:
                total += 1
        if total == 2:
            print('{0:d} is a prime'.format(num))
        else:
            print('{0:d} is NOT a prime'.format(num))

prime_numer_test()
