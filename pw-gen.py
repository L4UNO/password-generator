import random

print("****************************\nPlain and simple password generator\n****************************")

char_qty = int(input("How many characters do you want? "))

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
        "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T","U", "V", "W", "X",
        "Y", "Z", "0", "1", "2", "3","4", "5", "6", "7",
        "8", "9", "?", "!", "%", "/","&", "#", "(", ")"]

pw = []
pw_str = str("")


for i in range (0, 5):
    pw_str = ""
    pw = []
    for i in range (char_qty):
        tmp = random.randint(0, len(chars)-1)
        pw.append(chars[tmp])

    for i in pw:
        pw_str += i

    print("\n{}".format(pw_str))

qty = len(chars) ** char_qty

print("\nWith these simple limitations, there's\n{} different variations for the password.".format(qty))
