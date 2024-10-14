###
#class Student:
 #   count_of_students = 0
  #  def __init__(self, height= 160):
   #     self.height = height
    #    Student.count_of_students +=1

#mykola = Student()

#Katia = Student(height=170)

#print(mykola.count_of_students)
#print(Student.count_of_students)


# class Student:
#     count_of_students = 0
#     def __init__(self, name= None, height =160):
#         self.name = name
#         self.height = height
#     def __del__(self):
#         print("Training is over")
#     def __bool__(self):
#         return self.name != None
#     def __len__(self):
#         return self.height
# nick = Student()
# print(nick.__len__())
# print(nick.__bool__())
# print(len(nick))
# print(bool())

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def calculate_area(self):
#         return 3.14159 * self.radius ** 2
#
#
#
# circle_1 = Circle(5)
# print(circle_1.calculate_area())

from datetime import datetime

class Knyga:
    def __init__(self, zagolovok, avtor, rik):
        self.zagolovok = zagolovok
        self.avtor = avtor
        self.rik = rik

    def what_year(self):
        current_year = datetime.now().year
        vik = current_year - self.rik
        return vik
knyha = Knyga("Art of war", "Sun' Tzu", -500)
print(f"Vik knygy --- {knyha.zagolovok}|{knyha.what_year()}")

print("hello")
print("Testing")
