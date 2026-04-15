# ==============================================
# Ezra Faira Azzahra Faisal
# J0403251030
# ==============================================

# ==============================================
# Latihan 1: Membuat Node Tree
# ==============================================

# class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
        
# membuat root
root = Node("A")

# menampilkan isi node
print("Data pada node:", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

#  ===== Pembahasan ========
# Class Node digunakan untuk membuat satu node pada binary tree
# yang memiliki 3 atribut: data (nilai), left (child kiri), dan right (child kanan)

# Saat membuat root = Node("A"):
# - data berisi "A"
# - left dan right otomatis None (karena belum punya child)

# Output:
# - root.data menampilkan nilai node yaitu "A"
# - root.left dan root.right bernilai None karena belum diisi child