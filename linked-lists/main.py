# data / next

class Node:
    def __init__(self , data , next: "Node" = None , prev: "Node" = None):
        self.data = data
        self.next = next
        self.prev = prev

node1 = Node(76)

print(id(node1))
