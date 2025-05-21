def discriminant(a: int | float, b: int | float, c: int | float) -> int | float:
    return b ** 2 - 4 * a * c

def larger_root(p: int | float, q: int | float) -> int | float:
    d = discriminant(1, p, q)
    return (-p + d ** 0.5) / 2

def smaller_root(p: int | float, q: int | float) -> int | float:
    d = discriminant(1, p, q)
    return (-p - d ** 0.5) / 2


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))

-2.5
1
print(smaller_root(2, 1))
print(larger_root(2, 1))