def kandidat(data):
    terurut = []
    for i in range(len(data)):
        terurut.append([data[i], i])

    # Algoritma Selection Sort (dimodifikasi untuk list of lists)
    n = len(terurut)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            # Bandingkan nilai (indeks 0 dari tuple/list)
            if terurut[j][0] > terurut[max_index][0]:
                max_index = j
                
        # Swap seluruh paket (nilai dan indeks aslinya)
        terurut[i], terurut[max_index] = terurut[max_index], terurut[i]
    
    return terurut[:5]

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
hasil = kandidat(data)
print(hasil)

print("Lima kandidat tertinggi:")
for nilai, indeks in hasil:
    print(f"Nilai: {nilai} (Indeks Asli: {indeks})")