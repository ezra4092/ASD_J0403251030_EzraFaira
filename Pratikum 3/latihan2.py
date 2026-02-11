# Kode mencari node tertentu di single circular linked list
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

    def find_node(self, key):
        if not self.head:
            print("List kosong")
            return
        temp = self.head
        while True:
            if temp.data == key:
                print("Elemen", temp.data, "ditemukan dalam Circular Linked List")
                return
            temp = temp.next
            if temp == self.head:
                break
        print("Elemen", key, "tidak ditemukan dalam Circular Linked List")


cll = CircularSinglyLinkedList()
input_data = input("Masukkan elemen ke dalam Circular Linked List (pisahkan dengan koma): ")
if input_data:  
    elemen_list = [int(x.strip()) for x in input_data.split(",")]
    for elemen in elemen_list:
        cll.insert_at_end(elemen)
cari_input = input("Masukkan elemen yang ingin dicari: ").strip()
if cari_input: 
    cari = int(cari_input)
    cll.find_node(cari)
else:
    print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")

