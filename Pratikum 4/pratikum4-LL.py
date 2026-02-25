# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1

# Implementasi Dasar: Node pada Linked list 
# ===========================================

# membuat class node (merupakan unit dasar dari linked list)
class Node:
    def __init__(self, data): # ini adalah konstruktor
        self.data = data #menyimpan nilai/data
        self.next = None #pointer ke node berikutnya


Node("A") # proses memanggil konstruktor, dengan cara memanggil nama classnya

# membuat node satu persatu
nodeA =Node("A") 
nodeB =Node("B") 
nodeC =Node("C") 

# menghubungkan node: A -> B -> C
nodeA.next = nodeB
nodeB.next = nodeC

# menentukan head node
head = nodeA

# Traversal: menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data)
    current = current.next 

# ===========================================
# Implementasi Dasar: Linked List + Insert 
# ===========================================

class LinkedList:
    def __init__(self):
        self.head = None # awalnya kosong

    def hapus_awal(self): # konsep pop dalam stack
        data_terhapus = self.head.data  # peek dalam stack
        # menghapus = menggeser head
        self.head = self.head.next
        print("Node yang dihapus adalah", data_terhapus)
    
    def insert_awal(self,data): #konsep push pada stack
        # buat node baru
        nodeBaru = Node(data) # panggil class node

        # node baru menunjuk ke head lama
        nodeBaru.next = self.head

        # head pindah ke node baru
        self.head = nodeBaru

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

#ini udah termasuk stack
print("============List Baru=============")
ll = LinkedList() #instantiasi
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()