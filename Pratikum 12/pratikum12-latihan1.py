# =================================================
# Nama    : Ezra Faira
# NIM     : J0403251030
# =================================================

# =================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# =================================================

# representasi weighted graph menggunakan dictionary bersarang
graph = { 
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

print("Jalur 1: A -> B -> D:", jalur_1)  # tampilkan jalur 1
print("Jalur 2: A -> C -> D:", jalur_2)  # tampilkan jalur 2

if jalur_1 < jalur_2:  # bandingkan jalur
    print("Jalur terpendek adalah A -> B -> D") 
else:
    print("Jalur terpendek adalah A -> C -> D")
    
# Pertanyaan analisis
# 1. Berapa total bobot jalur A -> B -> D?  jawab: 9

# 2. Berapa total bobot jalur A -> C -> D?  jawab: 3

# 3. Jalur mana yang dipilih sebagai jalur terpendek? jawab: A -> C -> D

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
# jawab: Jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit karena yang dihitung dalam weighted graph adalah total bobot (weight), bukan jumlah langkah.

# Setiap edge bisa memiliki nilai bobot yang berbeda. Jadi walaupun suatu jalur lebih pendek secara jumlah edge, total biayanya bisa lebih besar jika bobotnya lebih tinggi.
