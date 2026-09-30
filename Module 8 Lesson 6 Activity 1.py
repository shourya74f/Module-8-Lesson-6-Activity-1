class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Cricket- Player: {self.__player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} hits a six!")
    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score>=0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")

class Soccer:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score
    def info(self):
        print(f"Soccer- Player: {self.__player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} scores a goal!")
    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score>=0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")

c=Cricket("Virat Kohli", 75)
f=Soccer("Cristiano Ronaldo", 3)

for sport in (c, f):
    sport.info()
    sport.play()
    print()

c.__score=85
print(f"get_score() still shows: {c.get_score()}")

print("Updating scores...")
c.set_score(85)
f.set_score(5)