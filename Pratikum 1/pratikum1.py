#================================================
# Pratikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1: Membaca seluruh isi file
#================================================

# membuka file dengan mode read ("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("\n===Hasil Read===")
print("Tipe Data: ", type(isi_file)) 
print("Jumlah Karakter: ", len(isi_file))
print("Jumlah Baris: ", isi_file.count("\n")+1)

#Membuka file per baris
print("\n===Membaca File per Baris===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan baris baru \n
        print("Baris ke-:", jumlah_baris)
        print("Isinya :", baris)


#================================================
# Pratikum 1: Konsep ADT dan File Handling
#Latihan Dasar 2: Parsig baris menjadi kolom data
#================================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("\nNIM: ", nim, "| Nama: ", nama, "| Nilai: ", nilai )

# ===================================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 3: Membaca File dan Menyimpan ke List
# ===================================================

data_list = []

with open("data_mahasiswa.txt", "r", encoding="utf=8") as file:
    for baris in file:
        baris = baris.strip()
        
        # simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim, nama, int(nilai)])

print("\n=== Data Mahasiswa dalam List ===")
print(data_list)

print("\n=== Jumlah Record dalam List ===")
print("Jumlah Record", len(data_list))

print("\n==== Menampilkan Data Record Tertentu ====")
print("Contoh Record pertama: ", data_list[0])

# ===================================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 4: Membaca File dan Menyimpan ke Dictionary
# ===================================================

data_dict = {}
with open("data_mahasiswa.txt", "r", encoding="utf=8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        
        # simpan sebagai list "[nim, nama, nilai]"
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
print("\n==== Data mahasiswa dalam dictionary ====")
print(data_dict)