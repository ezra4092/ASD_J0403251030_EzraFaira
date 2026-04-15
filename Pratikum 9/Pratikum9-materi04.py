# ==============================================
# Ezra Faira Azzahra Faisal
# J0403251030
# ==============================================

# ==============================================
# Latihan 4; Traversal Inorder
# ==============================================

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
        
# embuat fungsi inorder: left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# membuat tree
root = Node("A")

# membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat childe level 2
root.left.left = Node("D")
root.left.right = Node("E")

print("Hasil Traversal Inorder")
inorder(root)

# ===== Pembahasan ========
# Traversal Inorder adalah cara mengunjungi node dengan urutan:
# Left → Root → Right

# Fungsi inorder():
# - Mengecek apakah node tidak kosong
# - Mengunjungi subtree kiri terlebih dahulu
# - Mencetak data node
# - Mengunjungi subtree kanan

# Pada tree di atas, urutan yang dihasilkan:
# D B E A C