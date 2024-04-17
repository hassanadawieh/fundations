

class Node:
    def __init__(self , data , next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self , head):
        self.head = head
        self.tail = head

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def insert_at_head(self, node):
        node.next = self.head 
        self.head = node    

    def insert_at_tail(self,node):
        current = self.head
        while(current.next is not None):
            current = current.next
        current.next = node

    def delete_node(self , node):
        current = self.head
        if current is node:
            self.head = current.next
        else:
            while current is not None:
                if current.next is node:
                    if current.next is self.tail:
                        self.tail = current
                    current.next = current.next.next
                else:
                    current = current.next    
         
            



        


node1 = Node(10)
node2 = Node(77)
node3 = Node(88)
node4 = Node(99)


my_linked_list = LinkedList(node1)

my_linked_list.insert_at_head(node2)
my_linked_list.insert_at_tail(node3)
my_linked_list.insert_at_tail(node4)
my_linked_list.delete_node(node4)

my_linked_list.print_list()



