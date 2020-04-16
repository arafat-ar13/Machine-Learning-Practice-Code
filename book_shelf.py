library_name = input("What do you want to call your library?: ").rstrip()
while len(library_name) == 0:
    library_name = input("You HAVE to enter your library's name: ").rstrip()

your_library = []

library_input = input("What book do you wanna add to your library: ").rstrip()
while len(library_input) == 0:
    library_input = input("You cannot get passed if you are not willing to let us know what goddamn book you wanna add: ").rstrip()

your_library.append(library_input)
print("Your book '%s' has been added. Your library now contains %s book" %
      (library_input, len(your_library)))


more_books = input("Do you wanna add more? ").lower()

item = "item"
if more_books == "yes" or more_books == "yeah":
    while more_books != "no":
        user_choice = input("Enter the book: ")
        your_library.append(user_choice)
        more_books = input("Continue? ")
        if more_books == "no":
          if len(your_library) > 1:
            item += 's'
            print("Okay it has stopped. Your library '%s' now has %s %s and they are %s" % (library_name, 
                len(your_library), item, your_library))
elif more_books == "no":
  print("Okay it has stopped. Your library '%s' now has %s %s and they are %s" % (library_name, 
         len(your_library), item, your_library))       