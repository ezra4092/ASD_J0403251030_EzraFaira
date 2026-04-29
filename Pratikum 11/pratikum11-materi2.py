#=================================================
#Nama   : Ezra Faira Azzahra Faisal
#NIM    : J0403251030
#Kelas  : B1
#=================================================

# ==========================================================
# Implementasi BFS
# ==========================================================

#Struktur Data Utk Membuat Antrian, kita gunakan dari library collections bawaan python
from collections import deque


#Implementasi Graph
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

def bfs(graph,start):    #Ini adlh fungsi utk melakukan penelusuran graph dengan BFS
    #Graph : dictionary yg menyimpan struktur dari daftar graph
    #Start: node awal penelusuran

    queue = deque()  #queue digunakan utk menyimpan node yg akan diproses
    visited = set()  #var yg digunakan utk menyimpan node yg sudah diproses

    queue.append(start)    #masukkan node awal ke queue

    visited.add(start)  #tandai node awal sbg node yg sudah dikunjungi

    while queue:
        node = queue.popleft()   #mengambil node paling depan dari queue

        #tampilkan node yg sedang dikunjungi
        print(node,end=" ")

        for neighbor in graph[node]:  #periksa semua tetangga dari node yg diambil
            if neighbor not in visited:
                visited.add(neighbor)     #tandai sbg sudah dikunjungi
                queue.append(neighbor)     #masukkan tetangga ke queue utk diproses nanti


#Menjalankan BFS dari node A
bfs(graph,'A')