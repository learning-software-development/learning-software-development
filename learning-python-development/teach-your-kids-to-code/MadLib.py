adjective = input("Please enter an adjective: ")
noun = input("Please enter a noun: ")
verb = input("Please enter a verb ending in -ed: ")
colour = input("Please enter a colour: ")
animal = input("Please enter an animal: ")
print("Your MadLib:")
print("The", adjective, noun, verb, "over the lazy brown dog.")
print("The {0} {1} {2} over the lazy {3} {4}.".format(adjective, noun, verb, colour, animal))
