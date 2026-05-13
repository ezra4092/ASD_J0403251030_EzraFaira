# =======================================
# Nama : Ezra Faira Azzahra Faisal
# NIM : J0403251030
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =======================================

# =======================================
# Implementasi Sederhana Algoritma Kruskal
# =======================================
# Daftar edge: (bobot, node1, node2)
edges = [
 (1, 'C', 'D'),  # Edge C-D dengan bobot 1
 (2, 'A', 'C'),  # Edge A-C dengan bobot 2
 (3, 'B', 'D'),  # Edge B-D dengan bobot 3
 (4, 'A', 'B'),  # Edge A-B dengan bobot 4
 (5, 'A', 'D')   # Edge A-D dengan bobot 5
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()  # Sort ascending berdasarkan bobot

mst = []  # Menyimpan edge yang terpilih dalam MST
total_weight = 0  # Menyimpan total bobot MST

connected = set()  # Menyimpan node yang sudah terhubung

for weight, u, v in edges:  # Iterasi setiap edge
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:  # Cek sederhana agar tidak membentuk siklus
        mst.append((u, v, weight))  # Tambahkan edge ke MST
        total_weight += weight  # Tambahkan bobot ke total
        connected.add(u)  # Tandai node u sudah terhubung
        connected.add(v)  # Tandai node v sudah terhubung
        
print("Minimum Spanning Tree:")  # Menampilkan judul output

for edge in mst:  # Loop setiap edge dalam MST
    print(edge)  # Cetak edge
    
print("Total bobot =", total_weight)  # Menampilkan total bobot MST

# =======================================
# Jawaban Analisis
# =======================================

# 1. Edge mana yang dipilih pertama kali? 
# Edge dengan bobot 1 (C, D) dipilih pertama kali karena memiliki bobot terkecil.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
# Karena algoritma Kruskal bertujuan untuk membangun MST dengan total bobot minimum, 
# sehingga edge dengan bobot paling kecil dipilih terlebih dahulu untuk memastikan bahwa 
# penambahan edge tersebut tidak akan meningkatkan total bobot secara signifikan.

# 3. Berapa total bobot MST yang dihasilkan?
# Total bobot MST yang dihasilkan adalah 6, yang merupakan jumlah dari bobot edge (C, D), (A, C), dan (B, D).

# 4. Mengapa edge tertentu tidak dipilih? 
# Edge tidak dipilih agar tree tidak membentuk cycle dalam MST.
