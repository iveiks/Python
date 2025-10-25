# Harjutus 09

for i in range(1,21):
    if i%15 == 0:
        print(i,"TIKTAK", end=" ")
    elif i%3 == 0:
        print(i,"TIK", end=" ")
    elif i%5 == 0:
        print(i,"TAK", end=" ")
    else:
        print(i)