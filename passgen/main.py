import random

def main(nr_letters, nr_symbols, nr_numbers):
    print('RUNNING MAIN')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "@",]

    password = ""
    for char in range(0, nr_letters):
        random_char = random.choice(letters)
        password = password + random_char
    for int in range(0, nr_numbers):
        random_int = random.choice(numbers)
        password = password + random_int
    for sym in range(0, nr_symbols):
        random_sym = random.choice(symbols)
        password = password + random_sym

    print(password)
    return password

# a = random.choice(random_char, random_int, random_sym)
# print(a)

# print(f"{nr_letters}, {nr_symbols}, {nr_numbers}")