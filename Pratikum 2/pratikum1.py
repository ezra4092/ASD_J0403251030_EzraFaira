# ===========================================================
# Pratikum 2: Konsep ADT dan File Handling (Studi kasus)
# Latihan 1: Membuat fungsi load data
# ===========================================================

nama_file = "data_mahasiswa.txt"

# membuat fungsi 
def baca_data(nama_file):
    data_dict = {} # inisialisasi data dict

    with open("data_mahasiswa.txt", "r", encoding="utf=8") as file:
        for baris in file:
            baris = baris.strip() # menghilangkan \n
            nim, nama, nilai = baris.split(",") # pecah menjadi data satuan
            
            # simpan sebagai list "[nim, nama, nilai]"
            data_dict[nim] = {
                "nama" : nama,
                "nilai" : int(nilai)
            }
    return data_dict

#memanggil fungsi baca_data
buka_data = baca_data(nama_file)
# print("jumlah data terbaca", len(buka_data))

# ===========================================================
# Pratikum 2: Konsep ADT dan File Handling (Studi kasus)
# Latihan 2: Membuat fungsi menampilkan data
# ===========================================================

def tampilkan_data(data_dict):

    if len(data_dict) == 0:
        print("Data Kosong")
        return
    # Membuat header tabel
    print("==== Daftar Mahasiswa ====")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    print("-" * 32)

    '''
    untuk tampilan yang rapi, atur f-string formating
    {'NIM' : <10} => tampilkan nim, rata kiri dengan lebar kolom 10 karakter
    {'Nama' : <12} => tampilkan nama, rata kiri dengan lebar kolom 12 karakter
    {'Nilai' : <5} => tampilkan nilai, rata kiri dengan lebar kolom 12 karakter
    '''

    for nim in sorted(data_dict):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai: >5}")
    
# memanggil fungsi menampilkan
# tampilkan_data(buka_data)

# ===========================================================
# Pratikum 2: Konsep ADT dan File Handling (Studi kasus)
# Latihan 3: Membuat fungsi mencari data
# ===========================================================

def cari_data(data_dict):
    # mencari data mahasiswa
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n ==== Data Mahasiswa Ditemukan ====")
        print(f"Nama : {nim_cari}" )
        print(f"Nama : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("Data tidak ditemukan")

# cari_data(buka_data)

# ===========================================================
# Pratikum 2: Konsep ADT dan File Handling (Studi kasus)
# Latihan 4: Membuat fungsi update data
# ===========================================================

def update_nilai(data_dict):
    nim = input("Masukkan NIM mahasiswa yang akan diupdate nilainya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka, update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus diantara 0 sampai 100, update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

# update_nilai(buka_data)



# ===========================================================
# Pratikum 2: Konsep ADT dan File Handling (Studi kasus)
# Latihan 5: Membuat fungsi menyimpan perubahan data ke file
# ===========================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai}\n")
simpan_data(nama_file, buka_data)
print("Data Berhasil Disimpan")

def main():
    # menjalankan fungsi 1 load data
    buka_data = baca_data(nama_file)

    while True:
        print("\n === Menu Data Mahasiswa ===")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan NIM")
        print("3. Update nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")

        pilihan = int(input("Pilihan menu: ").strip())

        if pilihan == 1:
            tampilkan_data(buka_data)
        elif pilihan == 2:
            tampilkan_data(buka_data)
            cari_data(buka_data)
        elif pilihan == 3:
            update_nilai(buka_data)
        elif pilihan == 4:
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan")
        elif pilihan == 0:
            print("Program Selesai")
            break
        else:
            print("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()

    

