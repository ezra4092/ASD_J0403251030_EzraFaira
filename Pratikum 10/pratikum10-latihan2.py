# =============================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Latihan 4 : Membuat BST yang tidak seimbang
# =============================================

class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan
        
# fungsi insert untuk BST        
def insert(root, data):
    # jika root kosong, buat node baru
    if root is None:
        return Node(data)
    
    # jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    # jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    return root

# fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

# fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level = 0, posisi = 'Root'):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, 'L')
        tampil_struktur(root.right, level + 1, 'R')
        
# ===========================================
# Program utama
# =============================================

root = None

# data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST: ")
preorder(root)

print("\n\nStruktur BST: ")
tampil_struktur(root)