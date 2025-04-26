# To-Do List Sederhana
def tampilkan_tugas():
    try:
        with open("tugas.txt", "r") as file:
            tugas = file.readlines()
            if len(tugas) == 0:
                print("Tidak ada tugas saat ini.")
            else:
                print("Daftar Tugas:")
                for idx, tugas_item in enumerate(tugas, start=1):
                    print(f"{idx}. {tugas_item.strip()}")
    except FileNotFoundError:
        print("Belum ada tugas, mulai dengan menambahkan tugas baru.")

def tambah_tugas():
    tugas_baru = input("Masukkan tugas baru: ")
    with open("tugas.txt", "a") as file:
        file.write(tugas_baru + "\n")
    print(f"Tugas '{tugas_baru}' berhasil ditambahkan.")

def hapus_tugas():
    tampilkan_tugas()
    try:
        tugas_ke_hapus = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        with open("tugas.txt", "r") as file:
            tugas = file.readlines()
        
        if 1 <= tugas_ke_hapus <= len(tugas):
            del tugas[tugas_ke_hapus - 1]
            with open("tugas.txt", "w") as file:
                file.writelines(tugas)
            print(f"Tugas nomor {tugas_ke_hapus} telah dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid, masukkan nomor tugas dengan benar.")
    except FileNotFoundError:
        print("Belum ada tugas yang disimpan.")

def main():
    while True:
        print("\nPilih aksi:")
        print("1. Tampilkan Daftar Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '1':
            tampilkan_tugas()
        elif pilihan == '2':
            tambah_tugas()
        elif pilihan == '3':
            hapus_tugas()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan To-Do List!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
