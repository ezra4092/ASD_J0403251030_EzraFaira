# =======================================
# Nama : Ezra Faira Azzahra Faisal
# NIM : J0403251030
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =======================================

# =======================================
# Implementasi Sederhana Algoritma Prim
# =======================================
import heapq  # Library untuk priority queue (heap)

graph = {
 'A': {'B': 4, 'C': 2, 'D': 5},  # Node A terhubung ke B, C, D
 'B': {'A': 4, 'D': 3},  # Node B ke A dan D
 'C': {'A': 2, 'D': 1},  # Node C ke A dan D
 'D': {'A': 5, 'B': 3, 'C': 1}  # Node D ke A, B, C
}

def prim(graph, start):
    visited = set([start])  # Menyimpan node yang sudah dikunjungi
    edges = []  # Heap untuk menyimpan edge kandidat

    for neighbor, weight in graph[start].items():  # Ambil semua tetangga dari node awal
        heapq.heappush(edges, (weight, start, neighbor))  # Masukkan ke heap

    mst = []  # Menyimpan hasil MST
    total_weight = 0  # Menyimpan total bobot

    while edges:  # Selama masih ada edge
        weight, u, v = heapq.heappop(edges)  # Ambil edge dengan bobot terkecil

        if v not in visited:  # Jika node tujuan belum dikunjungi
            visited.add(v)  # Tandai node sebagai dikunjungi
            mst.append((u, v, weight))  # Tambahkan ke MST
            total_weight += weight  # Tambahkan bobot

            for neighbor, w in graph[v].items():  # Ambil tetangga dari node baru
                if neighbor not in visited:  # Hindari node yang sudah dikunjungi
                    heapq.heappush(edges, (w, v, neighbor))  # Masukkan ke heap

    return mst, total_weight  # Mengembalikan hasil


mst, total = prim(graph, 'A')  # Jalankan Prim dari node A

print("Minimum Spanning Tree:")  # Judul output

for edge in mst:  # Loop setiap edge MST
    print(edge)  # Cetak edge

print("Total bobot =", total)  # Cetak total bobot

# =======================================
# Jawaban Analisis
# =======================================

# 1. Node awal apa yang digunakan? 
# Node awal yang digunakan adalah node 'A', karena algoritma Prim memulai prosesnya dari satu node awal yang dipilih.

# 2. Edge mana yang dipilih pertama kali?
# Edge dengan bobot 2 (A, C) dipilih pertama kali karena memiliki bobot terkecil di antara edge yang terhubung dengan node 'A'.

# 3. Bagaimana Prim menentukan edge berikutnya?
# Prim menentukan edge berikutnya dengan memilih edge dengan bobot terkecil yang menghubungkan node yang sudah berada 
# di dalam tree dengan node lain yang belum terhubung. Proses ini terus dilakukan hingga seluruh node pada graph saling terhubung
# tanpa membentuk cycle.

# 4. Berapa total bobot MST yang dihasilkan?
# Total bobot MST yang dihasilkan adalah 6, yang merupakan jumlah dari bobot edge (A, C), (C, D), dan (D, B).

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
# Perbedaan pendekatan Prim dan Kruskal terletak pada cara mereka membangun MST. Prim memulai dari satu node awal dan secara bertahap
# menambahkan edge dengan bobot terkecil yang menghubungkan node yang sudah berada di dalam tree dengan node lain yang belum terhubung. 
# Sementara itu, Kruskal memilih edge dengan bobot terkecil secara global tanpa memulai dari node tertentu, dan hanya menambahkan edge 
# jika tidak membentuk cycle. Prim lebih berfokus pada pengembangan tree dari node awal, sedangkan Kruskal lebih berfokus pada pemilihan edge secara global.
