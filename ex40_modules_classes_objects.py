import mymodule
# import myclasses

fruits = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
mymodule.sortByKeys(fruits)


print('#' * 50)
class MyClass(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


thing = MyClass()
thing.apple()
print(thing.tangerine)

print('#' * 50)
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print("Singing:")
        for line in self.lyrics:
            print(f"\t{line}")


happy_bday = ["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"]

bulls_on_parade = ["They rally around tha family",
                        "With pockets full of shells"]

song1 = Song(happy_bday)
song2 = Song(bulls_on_parade)

song1.sing_me_a_song()
song2.sing_me_a_song()

