from .human import Human

class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print('#' * 50)
        print('# GAME OVER')
        print('#' * 50)
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)
