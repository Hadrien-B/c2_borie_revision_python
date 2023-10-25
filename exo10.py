def tri_tableau(tab):
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = k


tab = [87, 45, 105, 3992, 2, 714, 99, 66]
tri_tableau(tab)
print("Les nombres triés:")
for i in range(len(tab)):
    print("% d" % tab[i])
