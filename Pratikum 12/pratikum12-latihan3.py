# =================================================
# Nama    : Ezra Faira
# NIM     : J0403251030
# =================================================

# =================================================
# Latihan 3: Implementasi Bellman-Ford
# =================================================

# weighted graph dengan bobot negatif
graph = { 
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 
 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
 
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1): 
 
        # Periksa semua edge 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
 
                # Jika jarak ke node saat ini sudah diketahui, 
                # dan ditemukan jarak yang lebih kecil ke neighbor, 
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
 
    return distances 
 
 
hasil = bellman_ford(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance) 

# Pertanyaan analisis
# 1. Berapa bobot langsung dari A ke B? jawab: 5

# 2. Berapa total bobot jalur A -> C -> B? jawab: 2

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B? jawab: A -> C -> B

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif? 
# jawab: Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena algoritma ini melakukan relaksasi edge secara berulang, sehingga dapat menangani perubahan jarak yang disebabkan oleh bobot negatif. Selain itu, Bellman-Ford juga dapat mendeteksi adanya siklus negatif dalam graph, yang tidak bisa dilakukan oleh Dijkstra.

# 5. Apa yang dimaksud dengan proses relaksasi edge? 
# jawab: Proses relaksasi edge adalah langkah dalam algoritma Bellman-Ford di mana jarak ke suatu node diperbarui jika ditemukan jalur yang lebih pendek melalui edge tertentu. Jika jarak ke node saat ini sudah diketahui, dan ditemukan jalur yang lebih pendek ke neighbor melalui edge tersebut, maka jarak ke neighbor akan diperbarui dengan nilai yang lebih kecil. Proses ini dilakukan berulang kali untuk semua edge dalam graph.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra? 
# jawab: Perbedaan utama antara Bellman-Ford dan Dijkstra adalah bahwa Bellman-Ford dapat menangani graph dengan bobot negatif, sedangkan Dijkstra tidak dapat. Bellman-Ford menggunakan pendekatan relaksasi edge secara berulang, sementara Dijkstra menggunakan priority queue untuk memproses node dengan jarak terkecil terlebih dahulu. Selain itu, Bellman-Ford memiliki kompleksitas waktu O(V * E), sedangkan Dijkstra memiliki kompleksitas waktu O((V + E) log V) dengan implementasi heap.
