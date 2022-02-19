"""
program perulangan mambaca buku dengan while sampai paham
"""

jumlah_buku = 10
print('ibu berkata, "baca semua bukumu"')
jumlah_baca = 0

jumlah_paham = 0
print(f'jumlah buku yang sudah di baca dan dipahami {jumlah_paham}')

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_paham == 9:
        print(f'buku ke {jumlah_paham + 1} belm paham')
    else:
        jumlah_paham = jumlah_paham + 1
        print(f'buku ke {jumlah_paham} sudah dibaca dan dipahami')

print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}')
if jumlah_paham == jumlah_buku:
    print('bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'bu, tidak semua buku bisa dipahami.'
          f' saya hanya bisa memahami {jumlah_paham} buku')
