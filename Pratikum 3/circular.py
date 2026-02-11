class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head # circular link ke dirinya sendiri
        else:
            temp = self.head
            while temp.next != self.head: # mencari node terakhir
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head # circular link ke head

    def display(self): 
        if not self.head:
            print("List is empty")
            return
        
        print("Circular Linked List Traversal")
        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("... (back to head)")

cll = CircularSinglyLinkedList()
cll.insert_at_end(3)
cll.insert_at_end(5)
cll.insert_at_end(13)
cll.insert_at_end(2)
cll.display()