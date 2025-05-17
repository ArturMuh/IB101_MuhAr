persons = {}

def add_friends(name_of_person, list_of_friends):
    if name_of_person not in persons:
        persons[name_of_person] = set()
    persons[name_of_person].update(list_of_friends)

def are_friends(name_of_person1, name_of_person2):
    return name_of_person2 in persons.get(name_of_person1, set())

def print_friends(name_of_person):
    if name_of_person in persons:
        sorted_friends = sorted(persons[name_of_person])
        print(' '.join(sorted_friends))
    else:
        print()

add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))