# class for node

class node:
    def __init__(self, datavalue):
        self.datavalue = datavalue
        self.next = None

# class for head node
class head:
    def __init__(self):
        self.head = None


# instance of node class
a = node(28)
b = node(44)
c = node(3)
d = node(98)

# instance for head class
h1 = head()

# declare the head node
h1.head = a

# declare next nodes
a.next = b
b.next = c
c.next = d
d.next = None

temp = a

# display the linked list
while temp is not None:
    if temp.next == None:
      print(temp.datavalue, end=" ---> Null")
    else:
        print(temp.datavalue, end=" --->> ")

    temp = temp.next











