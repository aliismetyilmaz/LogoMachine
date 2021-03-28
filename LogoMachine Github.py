
class Node:
    def __init__(self=None, name=None, info=None):
        self.name = name
        self.info = info
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, newname, newinfo):
        NewNode = Node(newname, newinfo)
        NewNode.next = self.head
        self.head = NewNode

    # Function to remove node
    def RemoveNode(self, Removename):
        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.name == Removename):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.name == Removename:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

    # Function to find node
    # This Function checks whether the value
    # x present in the linked list
    def search(self, name):
        # Initialize current to head
        current = self.head
        # loop till current not equal to None
        while current != None:
            if current.name == name:
                return True  # data found
            current = current.next
        return False  # Data Not found

    def find(self, name):
        # Initialize current to head
        current = self.head
        # loop till current not equal to None
        while current != None:
            if current.name == name:
                return current  # data found
            current = current.next
        return None  # Data Not found


#-/-/-/-/-/-/ Interface /-/-/-/-/-/-/#
# to seperate strins into its letters
def split(word):
    return [char for char in word]


# to check if there is any unvalid command in logoinfo
def check(list1):
    # traverse in the list
    for x in list1:
        if (x == "D"):
            continue
        elif(x == "R"):
            continue
        elif(x == "U"):
            continue
        elif(x == "L"):
            continue
        else:
            return False
    return True


def draw(x, y, logoinfo):
    xcor = 2*x-2  # niye -2 oluyo
    ycor = 2*y-2
    # create the base table
    n = 21
    a = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i % 2 == 0 and j % 2 == 0:
                a[i][j] = ". "
            else:
                a[i][j] = "u "
    # engrave the logo
    for x in range(len(logoinfo)):
        # draw the lines one by one
        if(logoinfo[x] == "D"):
            a[xcor+1][(ycor)] = "| "
            xcor = xcor+2
        elif(logoinfo[x] == "U"):
            a[xcor-1][ycor] = "| "
            xcor = xcor-2
        elif(logoinfo[x] == "R"):
            a[xcor][ycor+1] = "- "
            ycor = ycor+2
        elif(logoinfo[x] == "L"):
            a[xcor][ycor-1] = "- "
            ycor = ycor-2
        else:
            print("wrong command in the machine")
    # print the table
    for row in a:
        print(' '.join([str(elem) for elem in row]))


# create the linked list
list = SLinkedList()

while(True):
    val = input("Enter your command: ")
    val = val.upper()
    commands = val.split(" ")
    # print(commands)

    if(commands[0] == "LOGO"):
        # save the logo and its informations(DDRUL) in the linked list
        # "You can assume that the user does not use any logo name twice."
        logoname = commands[1]
        logoinfo = split(commands[2])
        # check if the logoinfo is valid
        if(check(logoinfo)):
            list.Atbegining(logoname, logoinfo)
            print(logoname + " defined")
        else:
            print("logo info is not valid")

    elif(commands[0] == "ENGRAVE"):
        # check if there is a logo with that name
        if(list.search(commands[1])):
            x = int(commands[2])
            y = int(commands[3])
            draw(x, y, list.find(commands[1]).info)
        else:
            print("There is no " + commands[1] + " in the system")

    elif(commands[0] == "SAME"):
        if(list.search(commands[1]) and list.search(commands[2])):
            if(same(commands[1], commands[2])):
                print("Yes")
            else:
                print("No")
        else:
            print("unvalid logo names")
    else:
        print("First command is not valid")
