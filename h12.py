# Harjutus 12

# 3. Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt.
# Funktsioon peaks algama algse saldoga ja võimaldama teha operatsioone: deposiit (raha lisamine) ja väljavõte (raha eemaldamine). Tagastage peale igat toimingut konto jääk.
# Funtsiooni parameetrid:
# algne_saldo: Algse saldo väärtus.
# toiming: String, mis tähistab tehtavat toimingut ('deposiit' või 'valjavote').
# summa: Summa, mida soovitakse lisada või eemaldada.
# Näide: Alustades algse saldoga 100, deposiidi toiminguga 50, peaks funktsioon konto_haldur tagastama uue saldo 150. Väljavõtte toiminguga 20 uus saldo oleks siis 130.
# Kirjutage selge dokumentatsioon, mis kirjeldab, kuidas algset saldot seada, kuidas toiminguid teostada ja millist tüüpi väärtusi tagastatakse.


def konto_haldur(tehing, raha, saldo):
    """
    Lisab või eemaldab summa pangakontolt

    Parameetrid:
        tehing (str): Tehingutüüp
        raha (int): Raha
        saldo(int): Konto seis

    Tagastab:
        int: Konto seisu
        
    Näide:
        >>> konto = konto_haldur("deposiit", 50, konto)
        konto = konto_haldur("maha", 250, konto)
    """


    if tehing == "deposiit":
        uus_saldo = konto + raha
    else:
        uus_saldo = konto - raha

    return uus_saldo

konto = 100

konto = konto_haldur("deposiit", 50, konto)
konto = konto_haldur("deposiit", 500, konto)
konto = konto_haldur("maha", 250, konto)

print(konto)
print(konto_haldur.__doc__)