# =============================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Latihan : BST
# =============================================

class Node:
    def __init__(self, data):
        self.data = data        # menyimpan nilai/data pada node
        self.left = None        # pointer ke child kiri (default kosong)
        self.right = None       # pointer ke child kanan (default kosong)
        
def insert(root, data):
    if root is None:           # jika tree masih kosong
        return Node(data)      # buat node baru sebagai root
    
    if data < root.data:       # jika data lebih kecil dari root
        root.left = insert(root.left, data)   # masukkan ke subtree kiri
    elif data > root.data:     # jika data lebih besar dari root
        root.right = insert(root.right, data) # masukkan ke subtree kanan
    return root                # kembalikan root (tidak berubah jika data sama)
    
# mengisi data BST
root = None                    # inisialisasi tree kosong
data_list = [50, 30, 70, 20, 40, 50, 80]  # data yang akan dimasukkan ke BST

for data in data_list:         # looping setiap data dalam list
    root = insert(root, data) # insert data ke dalam BST

print("Data BST berhasil dibuat")  # output bahwa BST sudah terbentuk
    
# ========================================
# Latihan 2: Traversal BST
# ========================================

def inorder(root):
    if root is not None:      # jika node tidak kosong
        inorder(root.left)    # kunjungi subtree kiri
        print(root.data, end=' ')  # cetak data root
        inorder(root.right)   # kunjungi subtree kanan

print ("Hasil inorder: ")     # menampilkan judul output
inorder(root)                # memanggil fungsi inorder

# =========================================
# Latihan 3: Search di BST
# =========================================

def search(root, key):
    if root is None:         # jika node kosong (tidak ditemukan)
        return False
    
    if root.data == key:     # jika data ditemukan
        return True
    elif key < root.data:    # jika key lebih kecil
        return search(root.left, key)  # cari di subtree kiri
    else:                    # jika key lebih besar
        return search(root.right, key) # cari di subtree kanan
    
key = 100                    # data yang ingin dicari

if search(root, key):        # jika fungsi search mengembalikan True
    print("Data ditemukan")  # tampilkan pesan ditemukan
else: 
    print("Data tidak ditemukan")  # tampilkan pesan tidak ditemukan