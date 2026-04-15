def sequentialSearch (data, value):
    pos = 9
    found = False
    while pos <len (data) and not found:
        if data[pos] == value:
            found = True
        else:
            pos = pos + 1
    return found
data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print (sequentialSearch (data, 3))
print (sequentialSearch (data, 13))



# print("\n")
# def cariPertama(data, nilai):
#     pos = 0
#     while pos < len(data):
#         if data[pos] == nilai:
#             return pos  # Langsung berhenti dan kasih tau posisinya
#         pos += 1
#     return -1  # Jika sampai akhir tidak ketemu

# data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
# print(f"Indeks pertama nilai 2: {cariPertama(data, 2)}")
# print(f"Indeks pertama nilai 3: {cariPertama(data, 3)}")

# def cariSemua(data, nilai):
#     hasil_indeks = []
#     for pos in range(len(data)):
#         if data[pos] == nilai:
#             hasil_indeks.append(pos) # Simpan indeks ke dalam list
#     return hasil_indeks

# data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
# print(f"Seluruh posisi nilai 2: {cariSemua(data, 2)}")
# print(f"Seluruh posisi nilai 13: {cariSemua(data, 13)}")
