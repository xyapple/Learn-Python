import random
for a in range(1,6):
    for b in range(1,6):
        for c in range(1,6):
            for d in range(1, 6):
                if (a != b) and (b != c) and (c != d) and (a != d) and (a != c) and (d != b):
                    print (str(a)+str(b)+str(c)+str(d))
