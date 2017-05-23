num = int(input('Please enter a number: '))
a = 1

def sum_even(a, num):

        total = 0
        if num % 2 == 0:
            for i in range(a, num):
                if i % 2 == 0:
                    total += i
            return total + num
        else:
            for i in range(a, num):
                if i % 2 == 0:
                    total += i
            return total
print(sum_even(a, num))




