import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_small_letters = random.randint(4, 6)
nr_capital_letters = random.randint(1, 3)
nr_symbols = random.randint(1, 3)
nr_numbers = random.randint(1, 3)


class RandomPassword:

    def __init__(self):
        self.password_list = []
        self.password_str = ""

    def get_password(self):

        for l in range(0, nr_small_letters):
            self.password_list.append(small_letters[random.randint(0, len(small_letters) - 1)])

        for L in range(0, nr_capital_letters):
            self.password_list.append(capital_letters[random.randint(0, len(capital_letters) - 1)])

        for s in range(0, nr_symbols):
            self.password_list.append(symbols[random.randint(0, len(symbols) - 1)])

        for n in range(0, nr_numbers):
            self.password_list.append(numbers[random.randint(0, len(numbers) - 1)])

        random.shuffle(self.password_list)

        for i in range(0, len(self.password_list)):
            self.password_str += self.password_list[i]

        return self.password_str
