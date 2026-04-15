#sequential search
def cariPertama(data, nilai):
    pos = 0
    while pos < len(data):
        if data[pos] == nilai:
            return pos  # Langsung berhenti dan kasih tau posisinya
        pos += 1
    return -1  # Jika sampai akhir tidak ketemu

def cariSemua(data, nilai):
    hasil_indeks = []
    for pos in range(len(data)):
        if data[pos] > nilai:
            hasil_indeks.append(pos) # Simpan indeks ke dalam list
    return hasil_indeks

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
print(f"Indeks yang nilainya 33: {cariPertama(data, 33)}")
print(f"Indeks yang nilainya diatas 33: {cariSemua(data, 33)}")

# binary search
def binary_search_lebih_dari(data_awal, target):
    # 1. Bungkus dengan indeks asli agar tidak hilang saat sorting
    data_indexed = [[data_awal[i], i] for i in range(len(data_awal))]
    
    # 2. WAJIB SORT berdasarkan nilai (elemen ke-0)
    data_indexed.sort(key=lambda x: x[0])
    
    # 3. Binary Search untuk mencari posisi 'target'
    low = 0
    high = len(data_indexed) - 1
    posisi_ketemu = -1
    
    while low <= high:
        mid = (low + high) // 2
        if data_indexed[mid][0] == target:
            posisi_ketemu = mid
            break
        elif data_indexed[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    # 4. Ambil semua indeks asli dari posisi setelah target ditemukan
    indeks_asli_diatas_33 = []
    if posisi_ketemu != -1:
        # Kita mulai dari posisi_ketemu + 1 sampai akhir list
        for i in range(posisi_ketemu + 1, len(data_indexed)):
            indeks_asli_diatas_33.append(data_indexed[i][1])
            
    return posisi_ketemu, indeks_asli_diatas_33

# Data awal
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
target = 33

pos_di_sort, hasil_indeks = binary_search_lebih_dari(data, target)

print(f"\nData asli: {data}")
print(f"Indeks asli yang nilainya > {target}: {hasil_indeks}")

# Pembuktian
print("Nilai-nilainya adalah:", [data[i] for i in hasil_indeks])
