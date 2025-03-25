kol_knig_bibloitecka = int(input())
kol_king_na_leto = int(input())
v_bibliotecka = set()
na_leto = set()
try_set = set()
for i in range(kol_knig_bibloitecka):
    v_bibliotecka.add(input())
for i in range(kol_king_na_leto):
    na_leto.add(input())
for i in na_leto:
    intrsaction = v_bibliotecka & na_leto
    if intrsaction:
        print("YES")
        na_leto = intrsaction - v_bibliotecka
    else: print("NOT")