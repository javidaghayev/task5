from functions import student_average_point
from functions import gpa_calculator

print("Fennlerden topladiginiz ballari yazin (100 uzerinden) ")

english = float(input("Ingilis dili: "))
history = float(input("Tarix: "))
math = float(input("Riyaziyyat: "))
literature = float(input("Edebiyyat: "))

print("\nNeticeler: ")


gpa_calculator("Ingilis dili:", english)
gpa_calculator("Tarix:", history)
gpa_calculator("Riyaziyyat:", math)
gpa_calculator("Edebiyyat:", literature)



average = student_average_point(english, history, math, literature)
gpa_calculator("\nUmumi qiymet ortalamasi", average)


