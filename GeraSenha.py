import string
import secrets

def options():
    opt = input("(S/N)").upper()
    if opt == "S":
        return 1
    elif opt == "N":
        return 0
    else:
        print("Inválido")
        options()

while True:
    try:
        num = int(input("Tamanho da senha"))
    except ValueError:
        print("Tamanho da senha")
        continue
    print("Pode conter letras maiúsculas?")
    upperCase = options()
    print("Pode conter números?")
    numbers = options()
    print("Pode conter caracteres especiais?")
    specialCase = options()

    alphabet = string.ascii_uppercase*upperCase + string.ascii_lowercase \
               + string.digits*numbers + string.punctuation*specialCase

    pwd = ''
    for i in range(num):
      pwd += ''.join(secrets.choice(alphabet))

    print(pwd)
