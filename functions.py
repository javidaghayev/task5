#students_budget
def remaining_budget(revenues, expenses):
    return revenues - expenses







#bmi
def bmi_calculate(height, weight):
    bmi = round(weight / (height / 100)**2, 2)


    if bmi <= 18.5:
        print("Az çəki")
    elif bmi <= 24.9 and bmi > 18.5:
        print("Normal çəki")
    elif bmi <= 29.9 and bmi > 24.9:
        print("Artiq çəki")
    else:
        print("Piylenme")
    print(bmi)







#student_points
def student_average_point(*point):
    return (sum(point) / len(point))


def gpa_calculator(subject_name, gpa):
    if gpa >= 90 and gpa <=100:
        print(subject_name, gpa, "A")
    elif gpa >= 80:
        print(subject_name, gpa, "B")
    elif gpa >= 70:
        print(subject_name, gpa, "C")
    elif gpa >= 60:
        print(subject_name, gpa, "D")
    elif gpa < 60 and gpa >=0:
        print(subject_name, gpa, "F")
    else:
        print(False)
        