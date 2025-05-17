p = 3.14159

def circle_length(radius: int):
    return 2 * p * radius

def circle_area(radius: int):
    return p * radius ** 2

def main():
    radius = int(input())
    print(circle_length(radius), circle_area(radius))