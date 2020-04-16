user_string = input("Enter your string: ").split()
user_removal_word = input("Enter the word you want removed: ")

if user_removal_word in user_string:
    while user_removal_word in user_string:
        user_string.remove(user_removal_word)

    print(" ".join(user_string))
else:
    print("Your word is not in your string")
