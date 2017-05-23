def sqr1(x, num):
    assert x > 0, 'x must be non-nagtive, not ' + str(x)
    assert num > 0, 'number must be postive, not ' + str(num)

    low = 0
    high = max(x, 1.0)
##high = x
    guess = (low + high)/2.0

    counter = 1
    while (abs(guess ** 2 - x)) > num and (counter <= 100):
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        counter = counter +1
    return guess

def sqr2(y, n):
    assert y > 0, 'y must be non-nagtive, not ' + str(y)
    assert  n >0, 'n must be postive, not ' + str(n)

    low = 0
    high = y
    guess = (low + high)/2.0
    counter = 1
    while (abs(guess ** 2 - y)) > n and (counter <= 100):
        if guess ** 2 < y:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        counter = counter +1
    return guess