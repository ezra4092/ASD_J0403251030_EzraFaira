# ==============================================
# Ezra Faira Azzahra Faisal
# J0403251030
# ==============================================

# ==============================================
# Latihan 3: Traversal Preorder 
# ==============================================

# class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
        
# membuat tree
root = Node("A")

# membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat childe level 2
root.left.left = Node("D")
root.left.right = Node("E")

print("Hasil Traversal Preorder")
preorder(root)

# ===== Pembahasan ========
# Traversal Preorder adalah cara mengunjungi node dengan urutan:
# Root → Left → Right

# Fungsi preorder():
# - Mengecek apakah node tidak kosong
# - Mencetak data node saat ini
# - Mengunjungi subtree kiri
# - Mengunjungi subtree kanan

# Pada tree di atas, urutan yang dihasilkan:
# A B D E C
