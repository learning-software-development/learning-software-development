# Classes and objects

class GameCharacter:
    # attributes
    name = ""
    health = 100
    position = 0

    # initializer
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # behaviours
    def move_by(self, amount):
        self.position += amount

    def heal_self(self, by_amount):
        self.health += by_amount
        if self.health > 100:
            self.health = 100


new_character = GameCharacter("Monster", 50)
print(new_character.name)
print(new_character.health)
print(new_character.position)

new_character.move_by(10)
print(new_character.position)

new_character.health = 80
print(new_character.health)
new_character.heal_self(40)
print(new_character.health)
