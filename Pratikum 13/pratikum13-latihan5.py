# =======================================
# Nama : Ezra Faira Azzahra Faisal
# NIM : J0403251030
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# =======================================

# =======================================
# Tugas Mandiri: Buat Program MST dengan Kasus Baru
# =======================================

# Kasus 1. Jaringan Jalan Antar Kota menggunakan Algoritma Prim

import heapq  # Library untuk priority queue (heap)

# Representasi graph berdasarkan data soal
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},  # Bogor terhubung ke Jakarta & Depok
    'Jakarta': {'Bogor': 5, 'Depok': 3, 'Bandung': 6},  # Jakarta ke 3 kota
    'Depok': {'Bogor': 2, 'Jakarta': 3, 'Bandung': 4},  # Depok ke 3 kota
    'Bandung': {'Jakarta': 6, 'Depok': 4}  # Bandung ke Jakarta & Depok
}

def prim(graph, start):
    visited = set([start])  # Menyimpan node yang sudah dikunjungi
    edges = []  # Heap untuk menyimpan kandidat edge

    # Masukkan semua edge dari node awal ke heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))  # Push ke heap

    mst = []  # Menyimpan edge hasil MST
    total_weight = 0  # Menyimpan total bobot MST

    while edges:  # Selama masih ada edge
        weight, u, v = heapq.heappop(edges)  # Ambil edge dengan bobot terkecil

        if v not in visited:  # Jika node tujuan belum dikunjungi
            visited.add(v)  # Tandai sebagai dikunjungi
            mst.append((u, v, weight))  # Tambahkan ke MST
            total_weight += weight  # Tambahkan ke total bobot

            # Tambahkan edge dari node baru ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:  # Hindari node yang sudah dikunjungi
                    heapq.heappush(edges, (w, v, neighbor))  # Tambahkan ke heap

    return mst, total_weight  # Kembalikan hasil


# Mulai dari Bogor
mst, total = prim(graph, 'Bogor')  # Jalankan algoritma Prim

print("Minimum Spanning Tree:")

for edge in mst:  # Tampilkan setiap edge MST
    print(edge)

print("Total bobot =", total)  # Tampilkan total bobot


# =======================================
# Jawaban Analisis
# =======================================

# 1. Kasus apa yang dipilih?
# Kasus yang dipilih adalah jaringan jalan antar kota,
# di mana node merepresentasikan kota dan edge merepresentasikan
# jalan dengan bobot berupa jarak antar kota.

# 2. Algoritma apa yang digunakan?
# Algoritma yang digunakan adalah algoritma Prim,
# yaitu algoritma greedy yang membangun MST dengan memilih
# edge berbobot terkecil dari node yang sudah dikunjungi.

# 3. Edge mana saja yang dipilih dalam MST?
# Edge yang terpilih adalah:
# - Bogor - Depok (2)
# - Depok - Jakarta (3)
# - Depok - Bandung (4)

# 4. Berapa total bobot MST?
# Total bobot MST adalah:
# 2 + 3 + 4 = 9

# 5. Mengapa edge tertentu tidak dipilih?
# Edge seperti Bogor - Jakarta (5) dan Jakarta - Bandung (6)
# tidak dipilih karena ada alternatif jalur dengan bobot lebih kecil
# yang sudah menghubungkan semua node, sehingga edge tersebut
# akan menambah biaya tanpa diperlukan (membentuk cycle).