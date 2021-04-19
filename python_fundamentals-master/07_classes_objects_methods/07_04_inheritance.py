'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''
class Movie():
    
    def __init__(self, title, year) -> None:
        self.title = title
        self.year = year

    def __str__(self) -> str:
        return f"{self.title}, {self.year}"

class RomCom(Movie):
    pass

class ActionMovie(Movie):
    def __init__(self, title, year, pg=13) -> None:
        super().__init__(title, year)
        self.pg = pg

    def __str__(self) -> str:
        return f"{super().__str__()}, pg {self.pg}"

about_time = RomCom("About Time", 2013)
matrix = ActionMovie("Matrix", 1999, pg=13)

print(about_time)
print(matrix)