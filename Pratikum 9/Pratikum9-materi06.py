# ==============================================
# Ezra Faira Azzahra Faisal
# J0403251030
# ==============================================

# ==============================================
# Latihan 6: Struktur Organisasi Perusahaan
# ==============================================

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
 
def preorder(node):
    if node is not None:
        print(node.data, end="")
        preorder(node.left)
        preorder(node.right) 
        
# membuat tree struktur organisasi
root = Node("Direktur")

# child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.right = Node("Staff 3")

print("Struktur Organisasi (preorder):")
preorder(root)

# ===== Pembahasan ========
# Tree digunakan untuk merepresentasikan struktur organisasi perusahaan

# Node "Direktur" adalah root (paling atas)
# "Manajer A" dan "Manajer B" adalah bawahan langsung (level 1)
# "Staff 1", "Staff 2", dan "Staff 3" adalah level di bawahnya

# Menggunakan traversal preorder (Root → Left → Right),
# sehingga urutan yang ditampilkan:
# Direktur → Manajer A → Staff 1 → Staff 2 → Manajer B → Staff 3

# Cocok digunakan untuk menampilkan struktur dari atas ke bawah