# =================================================
# Nama    : Ezra Faira
# NIM     : J0403251030
# =================================================

# =================================================
# Latihan 4: Studi Kasus dengan program shortest path
# Algoritma: Dijkstra
# =================================================

import heapq  # priority queue untuk memilih jarak paling kecil


# representasi graph berbobot menggunakan dictionary
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}


def dijkstra(graph, start):
    # inisialisasi jarak semua node = tak hingga
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # jarak ke node awal = 0

    # priority queue untuk memilih node dengan jarak terkecil
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # skip jika sudah ada jalur lebih optimal
        if current_distance > distances[current_node]:
            continue

        # cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  # hitung jarak baru

            # jika ditemukan jarak lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# node awal
start_node = 'Bogor'

# menjalankan algoritma
hasil = dijkstra(graph, start_node)


print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")


# Jawaban Analisis:
# 1. Node awal yang digunakan apa? jawab: Bogor

# 2. Node mana yang memiliki jarak paling kecil dari node awal? jawab: Depok (2)

# 3. Node mana yang memiliki jarak paling besar dari node awal? jawab: Bandung (8)

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus ini:
#Jawab:
#Algoritma Dijkstra bekerja dengan cara memilih node dengan jarak terkecil
#dari node awal, lalu memperbarui jarak ke semua tetangganya jika ditemukan
#jalur yang lebih pendek. Proses ini diulang sampai semua node telah diproses,
#sehingga diperoleh jarak terpendek dari Bogor ke semua kota lain.