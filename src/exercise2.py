

a = int(input("a"))

b = int(input("b"))

c = int(input("c"))

l= [a, b, c]

result = []
# len(L) returns the number of items in the list

for i in range (len(l)):
    result.append(max(l))
    l.remove(max(l))

print(result)
