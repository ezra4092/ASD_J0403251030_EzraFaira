# =======================================
# Nama : Ezra Faira Azzahra Faisal
# NIM : J0403251030
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =======================================

# =======================================
# Studi Kasus: Jaringan Kabel Antar Gedung
# =======================================

# Daftar edge: (bobot, node1, node2)
edges = [
 (4, 'Gedung A', 'Gedung B'),  # Edge A-B dengan bobot 4
 (2, 'Gedung A', 'Gedung C'),  # Edge A-C dengan bobot 2
 (3, 'Gedung B', 'Gedung D'),  # Edge B-D dengan bobot 3
 (4, 'Gedung C', 'Gedung D'),  # Edge C-D dengan bobot 4
 (5, 'Gedung A', 'Gedung D')   # Edge A-D dengan bobot 5
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()  # Sort ascending berdasarkan bobot

mst = []  # Menyimpan edge yang terpilih dalam MST
total_weight = 0  # Menyimpan total bobot MST

connected = set()  # Menyimpan node yang sudah terhubung

for weight, u, v in edges:  # Iterasi tiap edge
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:  # Cek sederhana (bukan cycle kompleks)
        mst.append((u, v, weight))  # Tambahkan edge ke MST
        total_weight += weight  # Tambahkan bobot ke total
        connected.add(u)  # Tandai node u sudah terhubung
        connected.add(v)  # Tandai node v sudah terhubung
        
print("Minimum Spanning Tree:")

for edge in mst:  # Menampilkan hasil MST
    print(edge)
    
print("Total bobot =", total_weight)  # Menampilkan total bobot


# =======================================
# Jawaban Analisis
# =======================================

# 1. Algoritma apa yang digunakan?
# Algoritma yang digunakan adalah pendekatan mirip Kruskal, karena edge diurutkan
# dari bobot terkecil lalu dipilih satu per satu untuk membentuk MST.
# Namun, ini bukan Kruskal murni karena tidak menggunakan Union-Find
# dan pengecekan cycle masih sederhana.

# 2. Edge mana saja yang dipilih?
# Edge yang terpilih dalam MST adalah:
# - Gedung A - Gedung C (2)
# - Gedung B - Gedung D (3)
# - Gedung A - Gedung B (4)

# 3. Berapa total biaya minimum?
# Total bobot minimum yang diperoleh adalah:
# 2 + 3 + 4 = 9

# 4. Mengapa MST cocok digunakan pada kasus ini?
# MST cocok karena digunakan untuk menghubungkan semua gedung
# dengan biaya kabel seminimal mungkin tanpa membuat siklus (cycle),
# sehingga efisien dan tidak ada jalur yang redundan.