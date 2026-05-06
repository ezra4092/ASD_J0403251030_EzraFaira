# =================================================
# Nama    : Ezra Faira
# NIM     : J0403251030
# =================================================

# =================================================
# Implementasi Algoritma bellman-ford
# =================================================

def bellman_ford(graph, start):  # fungsi utama Bellman-Ford
    distances = {node: float('inf') for node in graph}  # jarak awal semua node = tak hingga
    distances[start] = 0  # jarak dari start ke dirinya sendiri = 0
    
    # relaksasi berulang
    for _ in range(len(graph) - 1):  # ulang sebanyak (V-1) kali
        for node in graph:  # cek tiap node
            for neighbor, weight in graph[node].items():  # cek tetangga & bobot
                if distances[node] + weight < distances[neighbor]:  # jika lebih kecil
                    distances[neighbor] = distances[node] + weight  # update jarak
    
    return distances  # hasil jarak terpendek

# Algoritma Bellman-Ford digunakan untuk mencari jarak terpendek dari satu node ke semua node lain, bahkan jika ada bobot negatif.
