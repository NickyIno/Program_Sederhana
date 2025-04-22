# Program untuk mengkonversi suhu antara Celsius, Fahrenheit, dan Kelvin

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def main():
    print("Pilih konversi suhu yang diinginkan:")
    print("1. Celsius ke Fahrenheit")
    print("2. Celsius ke Kelvin")
    print("3. Fahrenheit ke Celsius")
    print("4. Fahrenheit ke Kelvin")
    print("5. Kelvin ke Celsius")
    print("6. Kelvin ke Fahrenheit")

    pilihan = int(input("Masukkan pilihan (1/2/3/4/5/6): "))

    suhu = float(input("Masukkan suhu: "))

    if pilihan == 1:
        print(f"{suhu}° Celsius = {celsius_to_fahrenheit(suhu)}° Fahrenheit")
    elif pilihan == 2:
        print(f"{suhu}° Celsius = {celsius_to_kelvin(suhu)} Kelvin")
    elif pilihan == 3:
        print(f"{suhu}° Fahrenheit = {fahrenheit_to_celsius(suhu)}° Celsius")
    elif pilihan == 4:
        print(f"{suhu}° Fahrenheit = {fahrenheit_to_kelvin(suhu)} Kelvin")
    elif pilihan == 5:
        print(f"{suhu} Kelvin = {kelvin_to_celsius(suhu)}° Celsius")
    elif pilihan == 6:
        print(f"{suhu} Kelvin = {kelvin_to_fahrenheit(suhu)}° Fahrenheit")
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
