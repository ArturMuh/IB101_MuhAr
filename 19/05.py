scoring = {
    "Яблочко": 50,
    "Зеленое_кольцо": 25,
    "Внешнее_кольцо": {
        1: 8, 2: 6, 3: 42, 4: 1, 5: 10, 6: 5, 7: 15, 8: 20, 9: 17, 10: 12,
        11: 30, 12: 25, 13: 18, 14: 22, 15: 7, 16: 11, 17: 4, 18: 9, 19: 13, 20: 50
    },
    "Внутреннее_кольцо": {
        1: 2, 2: 9, 3: 56, 4: 3, 5: 15, 6: 8, 7: 20, 8: 12, 9: 25, 10: 7,
        11: 40, 12: 18, 13: 22, 14: 15, 15: 5, 16: 10, 17: 3, 18: 6, 19: 11, 20: 3
    }
}

# def score(*args):
#     if len(args) == 1:
#         return scoring.get(args[0], 0)
#     elif len(args) == 2:
#         ring, sector = args
#         return scoring.get(ring, {}).get(sector, 0)
#     else:
#         return 0

def score(ring: str, sector=None):
    if ring in ['Яблочко', 'Зеленое_кольцо']:
        return scoring.get(ring, 0)
    if sector is None:
        return 0
    return scoring.get(ring, {}).get(sector, 0)

print(score("Яблочко"))
print(score("Внешнее_кольцо", 1))

