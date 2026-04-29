#=================================================
#Nama   : Ezra Faira Azzahra Faisal
#NIM    : J0403251030
#Kelas  : B1
#=================================================

# ==========================================================
# Implementasi DFS
# ==========================================================

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

def dfs(graph,node, visited):   
    # fungsi untuk melakukan penelusuran graph menggunakan DFS
    # graph: dictioinary yang menyimpan graph
    # node: menyimpan node yang sedang dikunjungi
    # visited: menyimpan node yang sudah dikunjungi
    
    # tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)
    
    #tampilkan node yang sedang dikunjungi
    print(node, end=" ") 
    
    #periksa semua tetangga dari node yang sedang dikunjungi
    for neighbor in graph[node]: 
        
        # jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)
            
visited = set() # set untuk menyimpan node yang sudah dikunjungi

# menjalankan dfs dari A
dfs(graph,'A', visited)