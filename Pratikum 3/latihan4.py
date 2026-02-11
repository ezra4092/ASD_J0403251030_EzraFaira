class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    
    def gabung_list(list1, list2):
        if list1.head:  # jika list1 tidak kosong
            temp = list1.head
            while temp.next:  # cari node terakhir list1
                temp = temp.next
            temp.next = list2.head  # hubungkan node terakhir list1 ke head list2
        else:  # jika list1 kosong, gabungan jadi list2 saja
            list1.head = list2.head
        print("\nLinked List setelah digabungkan:")
        list1.display()

list1 = LinkedList()
list2 = LinkedList()
input_data1 = input("Masukkan elemen untuk Linked list 1 (pisahkan dengan koma): ")
if input_data1:  
    elemen_list = [int(x.strip()) for x in input_data1.split(",")]
    for elemen in elemen_list:
        list1.insert_at_end(elemen)
input_data2 = input("Masukkan elemen untuk Linked list 2 (pisahkan dengan koma): ")
if input_data2:  
    elemen_list = [int(x.strip()) for x in input_data2.split(",")]
    for elemen in elemen_list:
        list2.insert_at_end(elemen)
print("\nLinked list 1:")
list1.display()
print("\nLinked list 2:")
list2.display()

LinkedList.gabung_list(list1, list2)

