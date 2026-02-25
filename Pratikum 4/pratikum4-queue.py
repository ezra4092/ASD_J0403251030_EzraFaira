# ===========================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Kelas: TPL B1

# Implementasi Dasar: Queue berbasis Linked List 
# ===========================================

# membuat class node (merupakan unit dasar dari linked list)
class Node:
    def __init__(self, data): # ini adalah konstruktor
        self.data = data #menyimpan nilai/data
        self.next = None #pointer ke node berikutnya

# queue dengan 2 pointer: front dan rear
class QueueLL:
    def __init__(self):
        self.front = None # node paling depan
        self.rear = None # node paling belakang

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        # menambah data di belakang (rear)
        nodeBaru = Node(data)

        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        # jika queue tidak kosong: rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        # rear pindah ke node baru
        self.rear = nodeBaru

    def dequeue(self):
        # menghapus data dari depan
        # ambil data yang paling depan
        data_terhapus = self.front.data
        # geser front ke node berikutnya
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data_terhapus
    
    def tampilkan(self):
        # menampilkan isi queue dari head
        current = self.front
        print("Front", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Rear")

q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()