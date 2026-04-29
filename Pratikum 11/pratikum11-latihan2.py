#=================================================
#Nama   : Ezra Faira Azzahra Faisal
#NIM    : J0403251030
#Kelas  : B1
#=================================================

# ================================================
# Studi kasus dfs (eksplorasi lokasi)
# ================================================

# Implementasi DFS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Fungsi untuk melakukan penelusuran graph menggunakan DFS
def dfs(graph, node, visited):
    # graph: dictionary yang menyimpan graph
    # node: menyimpan node yang sedang dikunjungi   
    visited.add(node) 
    print(node, end=" ") 
    
    # periksa semua tetangga dari node yang sedang dikunjungi
    for neighbor in graph[node]: 
        # jika tetangga belum pernah dikunjungi
        if neighbor not in visited: 
            # lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

visited = set()
print("DFS dari A:")
dfs(graph, 'A', visited)

# Pertanyaan Analisis
# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# DFS menggunakan konsep rekursi (atau stack), sehingga selalu mengikuti satu jalur sampai mentok dulu sebelum kembali (backtracking).
# Makanya, dia akan terus “menyelam” ke node paling dalam sebelum pindah ke cabang lain.

# 2. Apa yang terjadi jika urutan neighbor diubah?
# Urutan hasil DFS akan ikut berubah.
# Karena DFS mengikuti urutan neighbor dari kiri ke kanan (sesuai list), jadi kalau urutannya diubah, jalur yang dieksplor duluan juga berubah.

# Contoh:
# ['B', 'C'] → A B D ...
# ['C', 'B'] → A C F ...

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama

# DFS: masuk dalam dulu
# Contoh hasil:
# ➝ A B D E C F
# BFS: per level (melebar)
# Contoh hasil:
# ➝ A B C D E F

# Perbedaan utama:
# DFS cocok untuk eksplorasi (menelusuri semua kemungkinan)
# BFS cocok untuk mencari jalur terdekat