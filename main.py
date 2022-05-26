import pstats


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    def change_name(self, new_name):
        self.name = new_name
    def change_age(self, new_age):
        int(new_age)
        self.age = new_age
    def add_track(self, new_track):
        self.tracks.append(new_track)
    def get_score(self):
        return self.score

bob = Student("Bob", 26, ["FE", "BE"], 20.90)
bob.change_name(input("What's your name: \n"))
bob.change_age(input("What's your age: \n"))
bob.add_track(input("What's your new track: \n"))
print(bob.get_score())


# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# # Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
