# =============================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# Latihan 6: Rotasi Kanan pada BST tidak seimbang
# =============================================

class Node:
    def __init__(self, data):
        self.data = data # nilai pada node
        self.left = None # child kiri
        self.right = None # child kanan


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
        
# fungsi rotasi kanan
def rotate_right(x):
    # x adalah root lama
    y = x.left # y adalah child kiri x
    T2 = y.right # subtree kanan milik y disimpan sementara
    
    # proses rotasi
    y.right = x # x menjadi child kanan dari y
    x.left = T2 # child kiri x diganti dengan T2
    
    # y menjadi root baru
    return y
        
# ===========================================
# Program utama
# =============================================

# membuat tree yang tidak seimbang:
# 10 - > 20 -> 30
root = Node(30) 
root.left = Node(20)  
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# melakukan rotasi kanan pada root
root = rotate_right(root)

print("\nPreorder setelah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan: ")
tampil_struktur(root)