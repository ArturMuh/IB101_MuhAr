def find_farthest_orbit(list_of_orbits: list[int | float]) -> tuple:
    orbits = [orb for orb in list_of_orbits if orb[0] != orb[1]]
    S = list(map(lambda a: a[0] * a[1] * 3.1415, orbits))
    return orbits[S.index(max(S))]
    # S = [a * b if a != b else 0 for a, b in list_of_orbits]
    # return list_of_orbits[S.index(max(S))]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
