# =======================================
# Nama : Ezra Faira Azzahra Faisal
# NIM : J0403251030
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =======================================

# =======================================
# Implementasi Spanning Tree
# =======================================
# Daftar edge graph
edges = [
 ('A', 'B'),  # Edge antara A dan B
 ('A', 'C'),  # Edge antara A dan C
 ('A', 'D'),  # Edge antara A dan D
 ('C', 'D'),  # Edge antara C dan D
 ('B', 'D')   # Edge antara B dan D
]

# Contoh spanning tree
spanning_tree = [
 ('A', 'C'),  # Edge yang dipilih dalam spanning tree
 ('C', 'D'),  # Menghubungkan C ke D
 ('D', 'B')   # Menghubungkan D ke B
]

print("Edge pada graph:")  # Menampilkan semua edge graph
for edge in edges:  # Loop setiap edge
    print(edge)  # Cetak edge

print("\nSpanning Tree:")  # Menampilkan spanning tree
for edge in spanning_tree:  # Loop setiap edge spanning tree
    print(edge)  # Cetak edge

print("\nJumlah edge graph =", len(edges))  # Hitung total edge graph
print("Jumlah edge spanning tree =", len(spanning_tree))  # Hitung edge MST

# =======================================
# Jawaban Analisis
# =======================================

# 1. Apa perbedaan graph awal dan spanning tree? 
# Graph awal memiliki 5 edge yang menghubungkan semua node, sedangkan spanning tree hanya memiliki 3 edge
# yang tetap menghubungkan semua node tanpa membentuk cycle. Spanning tree adalah subgraph dari graph awal 
# yang mencakup semua node dengan jumlah edge minimal.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# Spanning tree tidak boleh memiliki cycle karena tujuan utama dari spanning tree adalah untuk menghubungkan 
# semua node dengan jumlah edge minimal.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
# Jumlah edge dalam spanning tree selalu lebih sedikit dari graph awal karena spanning tree hanya mencakup edge
# yang diperlukan untuk menghubungkan semua node tanpa membentuk cycle.