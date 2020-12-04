class Character:

    def __init__(self, name: str, hp: int, level: int):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):

    def __init__(self, name: str, hp: int, level: int):
        super().__init__(name, hp, level)

    def speak(self):
        print("Hi there pal")

ted = NPC("ted", 100, 60)
ted.speak()