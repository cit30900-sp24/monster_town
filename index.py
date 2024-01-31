# from town import Town
# from monster import Monster
from monstertown import Town, Monster, Vampire, Mutant

def main():
    godzilla = Mutant('Godzilla', 50, 39000)

    muncie = Town('Muncie', 30000, 10000, 3500)

    dracula = Vampire('Dracula', 2, 175)

    kokomo = Town('Kokomo', 20000, 9000, 2000)

    print(godzilla.say_hello())
    print(muncie.description())

    muncie = godzilla.terrorize_town(muncie)

    print(muncie.description())

    muncie = godzilla.terrorize_town(muncie)

    print(muncie.description())

    muncie = godzilla.terrorize_town(muncie)

    print(muncie.description())

    print(kokomo.description())

    dracula.terrorize_town(kokomo)

    print(kokomo.description())

if __name__ == "__main__":
    main()