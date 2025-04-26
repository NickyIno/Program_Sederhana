# Kalkulator Sederhana
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y != 0:
        return x / y
    else:
        return "Tidak bisa dibagi dengan 0"

def main():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))

            if pilihan == '1':
                print(f"{num1} + {num2} = {tambah(num1, num2)}")
            elif pilihan == '2':
                print(f"{num1} - {num2} = {kurang(num1, num2)}")
            elif pilihan == '3':
                print(f"{num1} * {num2} = {kali(num1, num2)}")
            elif pilihan == '4':
                print(f"{num1} / {num2} = {bagi(num1, num2)}")

        except ValueError:
            print("Input salah, pastikan angka yang dimasukkan valid.")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
