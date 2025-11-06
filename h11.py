# Harjutus 11

# 3. Kirjuta funktsioon, mis kontrollib, kas kahest sõnast koosnev sõne algab sama tähega.
# print(sarnased_esitahed('Vapper Vares')) # peaks tagastama True
# print(sarnased_esitahed('Lahe Känguru')) # peaks tagastama False

def sarnased_esitahed(s):
    s1, s2 = s.split(" ")

    if (s1[0].capitalize()) == (s2[0].capitalize()):
        return True
    else:
        return False
    
print(sarnased_esitahed('vapper Vares')) # tagastab True
print(sarnased_esitahed('Lahe Känguru')) # tagastab False