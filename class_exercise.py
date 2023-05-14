from datetime import datetime

class Student:
    def __init__(self,name,year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}

    def add_attendace(day):
        if day == datetime.daytime.now():
            self.attendance.update({day:True})
        else:
            self.attendance.update({day:False})


    def add_grade(self,grade):
        if type(grade) == Grade:
            self.grades.append(grade)
    def get_average():
        self.avg = 0
        for notes in self.grades:
            self.avg += notes
        return self.avg/len(self.grades)

class Grade:
    minimum_passing = 65

    def __init__(self,score):
        self.score = score
    def is_passing():
        if self.score > self.minimum_passing:
            return self.score


roger = Student("Roger van der Weyden",10)
sandro = Student("Sandro Botticelli",12)
pieter = Student("Pieter Bruegel the Elder",8)
pieter.add_grade(Grade(100))