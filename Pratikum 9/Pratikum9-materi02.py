# ==============================================
# Ezra Faira Azzahra Faisal
# J0403251030
# ==============================================

# ==============================================
# Latihan 2: Membuat Binary Tree Sederhana
# ==============================================

# class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node
        self.left = None # child kiri
        self.right = None # child kanan
        
# membuat root
root = Node("A")

# membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat childe level 2
root.left.left = Node("D")
root.left.right = Node("E")

# membuat child level 3
root.right.left = Node("F")
root.right.right = Node("F")

# menampilkan isi node
print("Data pada node:", root.data)
print("Child kiri dari root:", root.left.data)
print("Child kanan dari root: ", root.right.data)
print("Child kiri dari B: ", root.left.left.data)
print("Child kanan dari B: ", root.left.right.data)
print("Child kiri dari C: ", root.right.left.data)
print("Child kanan dari C:", root.right.right.data)

#  ===== Pembahasan ========
# Binary Tree adalah struktur data berbentuk pohon dimana setiap node
# memiliki maksimal 2 child, yaitu child kiri (left) dan child kanan (right).

# Pada kode di atas:
# - Node "A" adalah root (akar dari tree)
# - Node "B" dan "C" adalah child level 1 dari root
# - Node "D" dan "E" adalah child dari "B"
# - Node "F" dan "F" adalah child dari "C"

# Cara mengakses node:
# - Gunakan .left untuk ke child kiri
# - Gunakan .right untuk ke child kanan

# Contoh:
# root.right.left berarti:
# dari root (A) → ke kanan (C) → ke kiri (F)

# root.right.right berarti:
# dari root (A) → ke kanan (C) → ke kanan (F)

# Sehingga kedua baris berikut menampilkan node F:
# print(root.right.left.data)
# print(root.right.right.data)



