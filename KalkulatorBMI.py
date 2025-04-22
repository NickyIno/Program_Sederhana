# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    tinggi_meter = tinggi / 100  # konversi cm ke meter
    bmi = berat / (tinggi_meter ** 2)  # rumus BMI
    return bmi

# Fungsi untuk menentukan kategori BMI
def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Input pengguna
print("Selamat datang di Kalkulator BMI!")
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))

# Hitung BMI
bmi = hitung_bmi(berat, tinggi)

# Tentukan kategori BMI
kategori = kategori_bmi(bmi)

# Output hasil
print(f"\nBMI Anda adalah {bmi:.2f}")
print(f"Kategori BMI Anda: {kategori}")
