x = 5
# if x >2:
#     print("Larager than 2.")
#     print("Still bigger")
# print("Done with 2.")

# for i in range(5):
#     print(i)
#     if i > 2:
#         print("Larager than 2")
#     print("Done with i", i)
# if x >1:
#     print('more than 1')
#     if x <100:
#         print('less than 100')
# print('all done')
'''
astr = 'Morning'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)
'''
# user input numer
user_input = input('Please enter a number: ')

try:
    isval = int(user_input)
except:
    isval = -1

if isval > 0:
    print('You have enter a numeric number. Nice work.')    
else:
    print('You did not enter a number.')
