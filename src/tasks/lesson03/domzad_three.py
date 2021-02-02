word = input("Введите строку: ")
if len(word) > 5:
    print(len(word))
elif len(word) < 5:
    print("Need more!")
elif len(word) == 5:
    print("It's five")
