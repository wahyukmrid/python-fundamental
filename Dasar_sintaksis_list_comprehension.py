print('\nperintah del')
daftar_buku = ['seven  habits', 'how to influence people', 'first things first', '4dx']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension')
daftar_buku = ['seven  habits', 'how to influence people', 'first things first', '4dx']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension start')
daftar_buku = ['seven  habits', 'how to influence people', 'first things first', '4dx']
del daftar_buku[0:-2] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension per step')
daftar_buku = ['seven  habits', 'how to influence people', 'first things first', '4dx']
del daftar_buku[0::2] #START:END:STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nmembuat list baru')
daftar_buku = ['seven  habits', 'how to influence people', 'first things first', '4dx']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nmembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension ganjil')
daftar_buku = ['seven  habits', 'how to influence people', 'first things first', '4dx']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension genap')
daftar_buku = ['seven  habits', 'how to influence people', 'first things first', '4dx']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension buang diujung')
daftar_buku = ['seven  habits', 'how to influence people', 'first things first', '4dx']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])
