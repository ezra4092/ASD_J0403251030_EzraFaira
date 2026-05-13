# =======================================
# Nama: Ezra Faira Azzahra Faisal
# NIM: J0403251030
# =======================================

# =======================================
# Implementasi Kruskal's Algorithm
# =======================================

# daftar edge: (bobot, node1, node2)
edges = [
    (1, 'A', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# mengurutkan edge berdasarkan bobot
edges.sort()

mst = [] # minimum spanning tree
total_weight = 0

# set sederhana untuk node yang sudah dipilih
connected = set()

for weight, u, v in edges:
    # jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected: 
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print(f"Total Bobot: {total_weight}")

# Algoritma Kruskal adalah algoritma Minimum Spanning Tree (MST) yang bekerja dengan memilih edge dengan bobot paling kecil 
# terlebih dahulu. Proses pemilihan edge dilakukan secara bertahap berdasarkan urutan bobot terkecil hingga seluruh node terhubung. 
# Namun, sebuah edge hanya akan ditambahkan ke dalam MST jika tidak membentuk cycle, sehingga graph tetap terhubung secara efisien 
# tanpa menghasilkan siklus. 