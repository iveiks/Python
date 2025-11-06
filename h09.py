# Harjutus 09

ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

lugeja = 0
r_kokku = 0
p_kokku = 0

for i in ev_data:
    # Vormindan tulpadena, :30 on tulba laius
    print(f"{i[0]:30} {i[1]:10} {i[2]:10}")
    if (i[1]).isnumeric()==True:
        r_kokku += int(i[1])
        p_kokku += int(i[2])
        lugeja += 1

print(f"Sõidu ulatus keskmine: {r_kokku/lugeja}")
print(f"Hind keskmine: {p_kokku/lugeja}")


print("Autod mis sõidavad üle 300")
for i in ev_data:
    if (i[1]).isnumeric()==True:     
        if int(i[1]) >= 300:
            print(i[0])


parim_hinnasuhe = 9999999999
parim_auto = ""

for i in ev_data:
    if (i[1]).isnumeric()==True:
        km_tasu = int(i[2]) / float(i[1])
        print(km_tasu)
        if km_tasu < parim_hinnasuhe:
            parim_hinnasuhe = km_tasu
            parim_auto = i[0]


print(f"Parim auto {parim_auto}")



for i in range(1,21):
    if i%15 == 0:
        print(i,"TIKTAK", end=" ")
    elif i%3 == 0:
        print(i,"TIK", end=" ")
    elif i%5 == 0:
        print(i,"TAK", end=" ")
    else:
        print(i)