import string
import random


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def random_password():

    length = int(input("Entrer la longeur du mot de passe: "))

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

random_password()
