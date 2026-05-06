# =================================================
# Nama    : Ezra Faira
# NIM     : J0403251030
# =================================================

# =================================================
# Implementasi Algoritma Dijkstra
# =================================================

import heapq  # untuk priority queue

graph = {  # representasi graph
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):  # fungsi dijkstra
    # menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}  # jarak awal = tak hingga
    
    # jarak node awal = 0
    distances[start] = 0  # start ke start
    
    # priority queue
    pq = [(0, start)]  # (jarak, node)
    
    while pq:  # selama queue tidak kosong
        current_distance, current_node = heapq.heappop(pq)  # ambil jarak terkecil
        
        # periksa semua tetangga
        for neighbor, weight in graph[current_node].items():  # cek neighbor
           distance = current_distance + weight  # hitung jarak baru
           
           # jika ditemukan jarak lebih kecil
           if distance < distances[neighbor]:  # cek apakah lebih optimal
               distances[neighbor] = distance  # update jarak
               heapq.heappush(pq, (distance, neighbor))  # masukkan ke queue
    
    return distances  # hasil akhir jarak

hasil = dijkstra(graph, 'A')  # jalankan dari A
print(hasil)  # tampilkan hasil

# Algoritma Dijkstra digunakan untuk mencari jalur terpendek dari satu node ke semua node lain dalam graph berbobot (tidak boleh ada bobot negatif).