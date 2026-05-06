# =================================================
# Nama    : Ezra Faira
# NIM     : J0403251030
# =================================================

# =================================================
# Latihan 2: Implementasi Dijkstra
# =================================================

import heapq  # untuk priority queue

# weighted graph dengan bobot positif
graph = { 
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    ''' fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra '''
    
    # semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    
    # jarak dari start ke start adalah 0
    distances[start] = 0
    
    # priority queue untuk menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]  
    
    while priority_queue:  # selama masih ada node yang belum diproses
        current_distance, current_node = heapq.heappop(priority_queue)  # ambil node dengan jarak terkecil
        
        # jika jarak saat ini lebih besar dari jarak yang sudah tercatat, maka proses dilewati
        if current_distance > distances[current_node]:
            continue
        
        # periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  # hitung jarak ke tetangga
            
            # jika jarak yang baru lebih kecil, update jarak dan masukkan ke priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances  # hasil akhir jarak

hasil = dijkstra(graph, 'A')  # jalankan algoritma dari node A
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)
    

# Pertanyaan analisis
# 1. Berapa jarak terpendek dari A ke B? jawab: 4

# 2. Berapa jarak terpendek dari A ke C? jawab: 2

# 3. Berapa jarak terpendek dari A ke D? jawab: 3 (2 + 1 melalui C)

# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
# jawab: Karena jarak dari A ke C adalah 2, dan dari C ke D adalah 1, sehingga total jarak adalah 3. Sedangkan jarak dari A ke B adalah 4, dan dari B ke D adalah 5, sehingga total jarak adalah 9.

# 5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
# jawab: priority_queue digunakan untuk menyimpan pasangan (jarak, node) dan memastikan bahwa node dengan jarak terkecil selalu diproses pertama.

# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif? 
# jawab: Karena algoritma Dijkstra mengasumsikan semua bobot edge adalah positif. Jika ada bobot negatif, algoritma ini tidak akan memberikan hasil yang benar karena ia tidak mempertimbangkan kemungkinan penurunan jarak yang dihasilkan oleh edge dengan bobot negatif.