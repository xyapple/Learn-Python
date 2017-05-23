import turtle

class PyList:
    def __init__(self):
        self.items = []

    def append(self,item):
        self.items = self.items + [item]

    # if we want to iterate over this sequence, we define the special method
    # called __iter__(self). Without this we’ll get "builtins.TypeError:
    # ’PyList’ object is not iterable" if we try to write
    # for cmd in seq:
    # where seq is one of these sequences. The yield below will yield an
    # element of the sequence and will suspend the execution of the for
    # loop in the method below until the next element is needed. The ability
    # to yield each element of the sequence as needed is called "lazy" evaluation # and is very powerful. It means that we only need to provide access to as
    # many of elements of the sequence as are necessary and no more.
    def __iter__(self):
        for c in self.items: yield c

def main():

    filename = input('Please enter drawing filename: ')

    # Create a Turtle Graphics window to draw in.
    t = turtle.Turtle()
    # The screen is used at the end of the program.
    screen = t.getscreen()

    # The next line opens the file for "r" or reading. "w" would open it for
    # writing, and "a" would open the file to append to it (i.e. add to the
    # end). In this program we are only interested in reading the file.

    file = open(filename, "r")

    # Create a PyList to hold the graphics commands that are
    # read from the file.
    graphicsCommands = PyList()
    command = file.readline().strip()
    while command != "":
    # Now we must read the rest of the record and then process it. Because
    # records are variable length, we’ll use an if-elif to determine which
    # type of record it is and then we’ll read and process the record.
    # In this program, processing the record means creating a command object
    # using one of the classes above and then adding that object to our
    # graphicsCommands PyList object.
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)

        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = CircleCommand(radius, width, color)

        elif command == "beginfill":
            color = file.readline().strip()
            cmd = BeginFillCommand(color)

        elif command == "endfill":
            cmd = EndFillCommand()

        elif command == "penup":
            cmd = PenUpCommand()

        elif command == "pendown":
            cmd = PenDownCommand()

        else:
            raise RuntimeError("Unknow Command: " + command)

        graphicsCommands.append(cmd)

        command = file.readline().strip()

    for cmd in graphicsCommands:
        cmd.draw(t)

        file.close()
        t.hr()
        screen.exitonclick()
        print("Program Excution Completed.")

if __name__ == "__main__":
    main()

#This is not working right



