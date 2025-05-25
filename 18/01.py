phrases = set ()

def parrot(phrase: str):
    if phrase in phrases:
        print(phrase)
    phrases.add(phrase)


parrot("Привет!")
parrot("Привет!")
parrot("Как дела?")
