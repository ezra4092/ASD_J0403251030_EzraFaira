nama_file = "data_barang.txt"

data_dict = {} #inisialisasi data dictionary
with open("data_barang.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline dan spasi di awal/akhir
        kode, barang, stok = baris.split(",") #parsing data berdasarkan koma
        data_dict[kode] = {
            "barang": barang,
            "stok": int(stok)
        }


#BACA DATA STOK YANG TERSEDIA
def baca_data(nama_file):
    data_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kode, barang, stok = baris.split(",")
            data_dict[kode] = {
                "barang": barang,
                "stok": int(stok)
            }
    return data_dict

buka_data = baca_data(nama_file)

def simpan_data(data_dict):
     with open(nama_file, "w", encoding="utf-8") as file:
            for kode in data_dict:
                barang = data_dict[kode]["barang"]
                stok = data_dict[kode]["stok"]
                file.write(f"{kode},{barang},{stok}\n")

#TAMPILKAN DATA STOK
def tampilkan_data(data_dict):
    
    if len(data_dict) == 0:
        print("Data Kosong")
        return
    
#Membuat Header Tabel
    print("\n======= Daftar Barang =======")
    print(f"{'Kode':10} | {'Nama Barang':<12} | {'Stok':>5}") #Mengatur Indentasi Pada Setiap Baris
    print("-" * 32)

    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["barang"]
        stok = data_dict[kode]["stok"]
        print(f"{kode:10} | {nama:<12} | {stok:>5}")


#PENAMBAHAN LIST BARANG 
def tambah_barang(data_dict):
    kode = input("Masukan Kode Barang:")
    if kode in data_dict:
        print("Data sudah ada, proses dibatalkan")
    else:
        nama = input("Masukan Nama Barang:" ).strip()
        stok = int(input("Masukan Stok Barang:").strip())
        data_dict[kode] = {
            "barang": nama,
            "stok": stok
        }
        simpan_data(data_dict)
        print("Data Berhasil Ditambahkan.")
 


#UPDATE STOCK
def update_stok(data_dict):
    kode_update = input("Masukkan Kode yang akan diupdate jumlah stoknya: ").strip()
    if kode_update not in data_dict:
        print("Kode tidak ditemukan, update dibatalkan.")
        return
    try:
        stok_baru = int(input("Masukkan jumlah stok baru: ").strip())
    except ValueError:
        print("Stok tidak valid, update dibatalkan.")
        return
    if stok_baru < 0:
        print("Stok dibawah 0, update dibatalkan.")

    stok_lama = data_dict[kode]["stok"]
    data_dict[kode_update]["stok"] = stok_baru
    simpan_data(data_dict)

    print(f"Update Selesai, Stok {kode_update} berubah dari {stok_lama} menjadi {stok_baru}")


#PENGHAPUSAN LIST DATA 
def hapus_data(data_dict):
    kode = input("Masukkan kode [BRGXX] yang akan dihapus nilainya: ")
    if kode not in data_dict:
        print("Barang tidak ditemukan, update dibatalkan.")
        return
    try:
        print("Barang tidak ditemukan, hapus dibatalkan")
    except ValueError:
        print("Stok tidak valid, update dibatalkan.")
        return
    target = data_dict[kode]
    sisa = [v for k, v in data_dict.items() if v != target]

    with open(nama_file, "w") as file:
        for k, v in data_dict.items():
            if v != target:
                file.write(f"{k},{v['barang']},{v['stok']}\n")
    data_dict.pop(kode)
    print("Data barang berhasil dihapus")
    tampilkan_data(data_dict)
    

def main(): 

    #Menjalankan fungsi 1 load data
    buka_data = baca_data(nama_file)


while True:
    print("\n=== HOMEPAGE DATA BARANG ===")
    print("1. Tampilkan Seluruh Barang")
    print("2. Tambah barang")
    print("3. Update stok barang")
    print("4. hapus data barang")
    print("0. Keluar")

    pilihan = input("Pilih menu (0-5): ")

    if pilihan == "1":
        tampilkan_data(buka_data)
    elif pilihan == "2":    
        tambah_barang(buka_data)
    elif pilihan == "3":
        update_stok(buka_data)
    elif pilihan == "4":
        hapus_data(buka_data)
    elif pilihan == "0":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()  #code agar home menu dijalankan lebih awal