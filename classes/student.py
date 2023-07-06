


class Student:
     school = "AkiraChix"
     def __init__(self,name,age,nationality):
        self.name= name
        self.age = age
        self.nationality = nationality
     def greet_student(self):
          return f"Hello {self.name }  welcome to {self.school}"
     


     def year_of_birth(self):
         year =2023 -self.age
         return f"Hello {self.name} you wer born in {year}"


