founded = False
text = ""
kol_strokes = 0
number_cot = 0
kolich_cats = 0
while "СТОП" != text:
    text = input()
    kol_strokes += 1
    if ('Кот' in text) or ('кот' in text):
        founded = True
        kolich_cats += 1
        if founded:
            number_cot = kol_strokes
if founded:
    print(kolich_cats,number_cot)
else:
    print(0,"-1")