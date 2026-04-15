# ==============================================
# Ezra Faira Azzahra Faisal
# J0403251030
# ==============================================

# ==============================================
# Latihan 5: Traversal Postorder
# ==============================================

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
        
# membuat fungsi postorder: left -> right -> root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")

# membuat tree
root = Node("A")

# membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat childe level 2
root.left.left = Node("D")
root.left.right = Node("E")

print("Hasil Traversal Postorder")
postorder(root)

# ===== Pembahasan ========
# Traversal Postorder adalah cara mengunjungi node dengan urutan:
# Left → Right → Root

# Fungsi postorder():
# - Mengecek apakah node tidak kosong
# - Mengunjungi subtree kiri
# - Mengunjungi subtree kanan
# - Mencetak data node terakhir

# Pada tree di atas, urutan yang dihasilkan:
# D E B C A