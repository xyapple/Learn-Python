'''
write a program which reads list of numbers until 'done' is entered.
Once 'done' is entered, print out total, count, and average of the numbers.
if the user enters anything other than a number, print an error message and skip 
to next number.
eg:

Enter a number: 4
Enter a number: 5
Enter a number: baad data
Invalid input
Enter a number: 7
Enter a number: done
Average: 5.3333
'''
def oneWay():
    count = 0
    total = 0
    while True:    
            user_input = input("Enter a number: ")
            if user_input.isdigit():
                user_input = int(user_input)
                count = count + 1   
                total = total + user_input           
                average = total / count
            
            elif user_input == 'done':
                break
            else:
                print('Sorry, your input is not a number, please enter a number.')

    print(user_input)
    print('count is:', count)
    print('total is: ', total)
    print('average is: ', average)
#oneWay()
###Another way to do this
def anotherWay():
    count = 0
    total = 0
    while True:
        inp = input("Enter a number: ")

        if inp == 'done':
            break
        if len(inp) < 1: #check for empty input
            break
        try:
            num = float(inp)
        except:
            print("Invalid input")
            continue
        count = count + 1
        total = total + num

        print(num, total, count)
    print("Average:", total/count)

anotherWay()