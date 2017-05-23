'''
# indefinite loop

fruit = 'banana'
index = 0
# for i in fruit:
#     if index < len(fruit):
#         index = index + 1
#         print(index, i)
while index < len(fruit):
    i = fruit[index]
    print(i)
    index = index + 1

# definite loop
another_fruit = 'pineapple'
for letter in another_fruit:
    print(letter)

'''
'''
parsing text Assignment
'''

text = "X-DSPAM-Confidence:    0.8475";

a = text.find(':')
b = float(text[a+5:])
print(b)

'''
another way to do it

'''
x = "X-DSPAM-Confidence:    0.8475";
pos = x.find(':')
print(x[pos+1:])
num = float(x[pos+1:])
print(num)