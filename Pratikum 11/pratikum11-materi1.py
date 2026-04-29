# =============================
# Implementasi Dasar Graph
# =============================

# struktur data untuk membuat antrian, kita gunakan dari library collection bawaan python
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
}

for node in graph:
    print(node, "->", graph[node])