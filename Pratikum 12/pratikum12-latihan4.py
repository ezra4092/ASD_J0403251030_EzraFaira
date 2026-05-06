# =================================================
# Nama    : Ezra Faira
# NIM     : J0403251030
# =================================================

# =================================================
# Latihan 4: Studi Kasus dengan program shortest path
# Algoritma: Dijkstra
# =================================================

import heapq  # priority queue
from turtle import distance  # (tidak dipakai)

# graph lokasi kampus
# bobot = waktu tempuh (menit)
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):  # fungsi dijkstra
    distances = {node: float('inf') for node in graph}  # jarak awal inf
    distances[start] = 0  # start = 0
    priority_queue = [(0, start)]  # queue awal
    
    while priority_queue:  # selama queue ada isi
        current_distance, current_node = heapq.heappop(priority_queue)  # ambil terdekat
        
        if current_distance > distances[current_node]:  # skip jika tidak optimal
            continue
        
        for neighbor, weight in graph[current_node].items():  # cek tetangga
            distance = current_distance + weight  # hitung jarak baru
            
            if distance < distances[neighbor]:  # jika lebih kecil
                distances[neighbor] = distance  # update jarak
                heapq.heappush(priority_queue, (distance, neighbor))  # masuk queue
    
    return distances  # hasil akhir

hasil = dijkstra(graph, 'Gerbang')  # jalankan dari Gerbang
print("Jarak terpendek dari Gerbang Kampus:")

for lokasi, jarak in hasil.items():  # tampilkan semua hasil
    print(lokasi, "=", jarak, "menit")  # output jarak
    
# Pertanyaan analisis 
# 1. Lokasi mana yang paling dekat dari Gerbang?  jawab: Kantin (2 menit)

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? jawab: 7 menit (Gerbang -> Kantin -> Lab -> Aula)

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. 
# jawab: Tidak selalu. Jalur langsung mungkin memiliki bobot yang lebih besar dibandingkan jalur yang melalui beberapa node. Dalam kasus ini, meskipun ada jalur langsung dari Gerbang ke Aula, jalur melalui Kantin dan Lab memberikan waktu tempuh yang lebih singkat.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini? 
# jawab: Dijkstra cocok digunakan karena graph ini memiliki bobot positif (waktu tempuh), dan kita ingin mencari jalur terpendek dari satu titik (Gerbang) ke semua titik lainnya. Dijkstra efisien untuk kasus seperti ini, di mana kita tidak memiliki bobot negatif dan ingin menemukan jarak terpendek.