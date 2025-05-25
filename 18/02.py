# daily_food = []
#
# def count_food(days: list [int]):
#     total = 0
#     for day in days:
#         if 1 <= day <= len(daily_food):
#             total += daily_food[day - 1]
#     return total
#
# daily_food = [0, 150, 150]
# print(count_food([1]))
# print(count_food([2, 3]))

def count_food(days: list[int]):
    return sum(daily_food[i - 1] for i in days if len(daily_food) > i >= 0)

daily_food = [0, 150, 150]
print(count_food([1]))