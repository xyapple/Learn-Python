import math


class solver:
    def demo(self):
        while True:
            a = int(input("a"))

            b = int(input("b"))

            c = int(input("c"))

            d = int(input("d"))

            e = float(b ** 2 + 4*a*c*d)
            if e >= 0:
                disc = math.sqrt(e)
                root1 = (-b + disc)/ (2*a)
                root2 = (-b - disc) / (2*a)
                print(root1, root2)
            else:
                print("error")

solver().demo()

