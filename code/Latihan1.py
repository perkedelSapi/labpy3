from random import random

def generate_random_numbers(n):
    count = 0  # Menyimpan jumlah bilangan acak yang sudah ditampilkan
    while count < n:
        # Generate bilangan acak
        value = random()
        # Cek jika nilai random lebih kecil dari 0.5
        if value < 0.5:
            print(value)  # Tampilkan nilai acak yang memenuhi syarat
            count += 1  # Tambahkan penghitung jika bilangan acak valid

# Meminta input dari pengguna untuk jumlah n
n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan: "))
generate_random_numbers(n)
