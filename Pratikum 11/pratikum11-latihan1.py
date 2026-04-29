#=================================================
#Nama   : Ezra Faira Azzahra Faisal
#NIM    : J0403251030
#Kelas  : B1
#=================================================

# ================================================
# Studi kasus bfs (jalur terdekat lokasi)
# ================================================

from collections import deque 
# Implementasi Graph
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

# Fungsi untuk melakukan penelusuran graph menggunakan BFS
def bfs(graph, start): 
    # graph: dictionary yang menyimpan graph
    # start: node awal penelusuran
    visited = set() 
    queue = deque([start]) 
    
    # tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start) 
    
    # proses BFS
    while queue:
        # ambil node paling depan dari queue 
        node = queue.popleft() 
        # tampilkan node yang sedang dikunjungi
        print(node, end=" ") 
        
        # periksa semua tetangga dari node yang sedang dikunjungi
        for neighbor in graph[node]: 
            # jika tetangga belum pernah dikunjungi
            if neighbor not in visited: 
                # tandai sebagai sudah dikunjungi
                visited.add(neighbor) 
                # masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor) 


print("BFS dari Rumah:") 
bfs(graph, 'Rumah')

# Pertanyaan Analisis
# 1. Node mana yang dikunjungi pertama?  
# Dalam algoritme BFS, proses selalu dimulai dari node yang didefinisikan sebagai start (dalam hal ini bfs(graph, 'Rumah')).
# Node ini akan masuk ke dalam antrean (queue) pertama kali dan langsung dicetak sebelum algoritme mulai mengeksplorasi tetangga-tetangganya ('Sekolah' dan 'Toko').

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?  
# Karena BFS menelusuri graph per level (selangkah demi selangkah).
# Artinya, node yang paling dekat dari titik awal akan dikunjungi lebih dulu, sehingga otomatis menemukan jalur terpendek (dalam jumlah langkah/edge).

# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
# Urutan hasil BFS akan berubah tergantung:
# - hubungan antar node (edge)
# - urutan tetangga (neighbor) di dalam list
# Contoh: kalau urutan ['Sekolah', 'Toko'] ditukar jadi ['Toko', 'Sekolah'],
# maka BFS juga akan mengunjungi Toko lebih dulu sebelum Sekolah.